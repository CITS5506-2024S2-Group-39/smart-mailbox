import RPi.GPIO as GPIO
import time

# GPIO setup code from 1.py
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

P1 = 4
P2 = 3
P3 = 2
P4 = 18
P5 = 17
P6 = 15
P7 = 14

GPIO.setup(P1, GPIO.OUT)
GPIO.setup(P2, GPIO.OUT)
GPIO.setup(P3, GPIO.OUT)

GPIO.setup(P4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(P5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(P6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(P7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

KEY = {
    (18, 4): '1',
    (18, 3): '2',
    (18, 2): '3',
    (17, 4): '4',
    (17, 3): '5',
    (17, 2): '6',
    (15, 4): '7',
    (15, 3): '8',
    (15, 2): '9',
    (14, 4): '*',
    (14, 3): '0',
    (14, 2): '#',
}

last = None

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

    key, = keys
    if last == key:
        return None

    last = key
    return key

# New password input using GPIO keypad
def input_password():
    password = ""
    while True:
        char = scan()
        if char:
            if char == '#':  # Input '#' to finish entering the password
                break
            elif char.isdigit():  # Only accept digits as password characters
                password += char
            print(f"Password so far: {password}")  # Debugging step to show progress
        time.sleep(0.1)
    return password

# List to store password
password_list = []

# Verify the password function
def verify_password(stored_password):
    input_pass = input_password()
    return input_pass == stored_password

# Main logic
if not password_list:
    print("Please enter a password:")
    first_password = input_password()
    password_list.append(first_password)  # Store the password

# Verify user input
print("Please re-enter your password for verification:")
is_correct = verify_password(password_list[0])
print("Password correct!" if is_correct else "Password incorrect!")
