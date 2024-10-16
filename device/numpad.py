import threading
import time
import RPi.GPIO as GPIO
from config import NumPadConfig
from shared import EventType, TimedValue

# Mapping of keypad positions to corresponding characters
KEY = {
    (NumPadConfig.ROW1, NumPadConfig.COL1): "1",
    (NumPadConfig.ROW1, NumPadConfig.COL2): "2",
    (NumPadConfig.ROW1, NumPadConfig.COL3): "3",
    (NumPadConfig.ROW2, NumPadConfig.COL1): "4",
    (NumPadConfig.ROW2, NumPadConfig.COL2): "5",
    (NumPadConfig.ROW2, NumPadConfig.COL3): "6",
    (NumPadConfig.ROW3, NumPadConfig.COL1): "7",
    (NumPadConfig.ROW3, NumPadConfig.COL2): "8",
    (NumPadConfig.ROW3, NumPadConfig.COL3): "9",
    (NumPadConfig.ROW4, NumPadConfig.COL1): "*",
    (NumPadConfig.ROW4, NumPadConfig.COL2): "0",
    (NumPadConfig.ROW4, NumPadConfig.COL3): "#",
}

# Stores the last detected key press to avoid duplicates when a key is held down
last = None


# Function to scan the keypad for key presses
def scan():
    global last
    keys = []

    # Check each column one by one
    for col in [NumPadConfig.COL1, NumPadConfig.COL2, NumPadConfig.COL3]:
        GPIO.output(col, GPIO.HIGH)
        for row in [
            NumPadConfig.ROW1,
            NumPadConfig.ROW2,
            NumPadConfig.ROW3,
            NumPadConfig.ROW4,
        ]:
            if GPIO.input(row) == GPIO.HIGH:
                key = KEY[(row, col)]
                keys.append(key)
        GPIO.output(col, GPIO.LOW)

    # If not exactly one key is pressed, ignore the input
    if len(keys) != 1:
        last = None
        return None

    # If the same key is being held down, ignore the input
    (key,) = keys
    if last == key:
        return None

    # Update the last key press and return the key
    last = key
    return key


# Thread function to continuously monitor the numpad for input
def daemon(interrupt, message_queue):
    print("Numpad monitoring thread started")

    password = TimedValue("")

    while not interrupt.is_set():
        time.sleep(0.1)

        # Skip if no input is detected
        char = scan()
        if not char:
            continue

        # Start a new input session if '*' is pressed
        if char == "*":
            password.set("")
            continue

        # If too much time have passed since the last key press,
        # User must press '*' to start a new input session
        (value, expired) = password.get_with_expired()
        if expired:
            print("Please press * to start input")
            continue

        # Add the current character to the password
        if char != "#":
            value += char
            password.set(value)
            print(f"Password so far: {value}")
            continue

        # Complete the password input if '#' is pressed
        # Reset the current input
        password.clear()

        # Submit the entered password
        message_queue.put((EventType.MailboxNumPadInput, value))

    print("Numpad monitoring thread stopped")


def init(interrupt, message_queue):
    # Configure the GPIO pins for the numpad
    GPIO.setup(NumPadConfig.COL1, GPIO.OUT)
    GPIO.setup(NumPadConfig.COL2, GPIO.OUT)
    GPIO.setup(NumPadConfig.COL3, GPIO.OUT)
    GPIO.setup(NumPadConfig.ROW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(NumPadConfig.ROW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(NumPadConfig.ROW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(NumPadConfig.ROW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Start the numpad monitoring thread
    thread = threading.Thread(target=daemon, args=(interrupt, message_queue))
    thread.start()
    return thread

