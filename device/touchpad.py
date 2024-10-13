import threading
import RPi.GPIO as GPIO
import time
import config 
import backend.password_manager 

# Define GPIO pin mappings 
P1 = 4
P2 = 3
P3 = 2
P4 = 18
P5 = 17
P6 = 15
P7 = 14

# Key mapping 
KEY = {
    (18, 4): "1",
    (18, 3): "2",
    (18, 2): "3",
    (17, 4): "4",
    (17, 3): "5",
    (17, 2): "6",
    (15, 4): "7",
    (15, 3): "8",
    (15, 2): "9",
    (14, 4): "*",
    (14, 3): "0",
    (14, 2): "#",
}

last = None

# Scanning the keypad
def scan():
    global last
    keys = []

    for col in [P1, P2, P3]:
        GPIO.output(col, GPIO.HIGH)
        for row in [P4, P5, P6, P7]:
            if GPIO.input(row):
                key = KEY[(row, col)]
                keys.append(key)
        GPIO.output(col, GPIO.LOW)

    if len(keys) != 1:
        last = None
        return None

    (key,) = keys
    if last == key:
        return None

    last = key
    return key

# Touchpad setup function
def setup_touchpad():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(P1, GPIO.OUT)
    GPIO.setup(P2, GPIO.OUT)
    GPIO.setup(P3, GPIO.OUT)

    GPIO.setup(P4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(P5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(P6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(P7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    print("Touchpad set up and ready to use.")

# Thread to monitor touchpad input
def daemon():
    print("Touchpad monitoring thread started")

    password = ""
    reset_mode = False  # Tracks whether we're resetting the PIN
    while  not config.interrupt.is_set():
        char = scan()
        if char:
            if char == "#":  # Input '#' to finish entering the password
                if reset_mode:
                    event = config.Event(event_type="touchpad_reset", data=password)
                    config.message_queue.put(event)  # Trigger a PIN reset event
                    reset_mode = False  # Exit reset mode after submission
                else:
                    event = config.Event(event_type="touchpad_pin", data=password)
                    config.message_queue.put(event)  # Submit the entered password
                password = ""  # Reset the password after submission

            elif char.isdigit():  # Only accept digits as password characters
                password += char
                print(f"Password so far: {password}")  # Debugging step to show progress

            elif char == "*":  # Trigger reset process if * is pressed
                next_char = scan()  # Check if the next key press is '#'
                if next_char == "#":
                    reset_mode = True  # Enable reset mode
                    print("Reset PIN requested")
            
        time.sleep(0.1)
    print("Touchpad monitoring thread stopped")

# Initialize the touchpad thread
def init():
    setup_touchpad()  # Set up the GPIO pins for the touchpad
    thread = threading.Thread(target=daemon)  # Start the touchpad daemon thread
    thread.start()

# Function to set a new PIN
def set_new_pin():
    print("Please enter a new PIN:")
    new_password_event =  config.message_queue.get()  # Wait for the new PIN input
    new_password = new_password_event.data

    print("Please re-enter the new PIN for confirmation:")
    confirm_password_event = config.message_queue.get()  # Wait for the confirmation PIN input
    confirm_password = confirm_password_event.data

    if new_password == confirm_password:
        backend.password_manager.store_password(new_password)  # Store the new PIN in the db
        print("New PIN set successfully.")
    else:
        print("PINs did not match. Please try again.")

# Function to reset the PIN
def reset_pin():
    stored_password = backend.password_manager.load_password()
    if stored_password is None:  #if password file is empty
        print("No PIN found. Please set a new one.")
        set_new_pin()
        return
    
    # Verify the existing PIN first
    print("Enter your current PIN to reset:")
    current_pin_event = config.message_queue.get()  # Wait for current PIN input

    if backend.password_manager.verify_password(current_pin_event.data):
        print("PIN verified. Proceeding to set a new PIN.")
        set_new_pin()  # Call to reset the PIN
    else:
        print("Incorrect PIN. Cannot reset.")
