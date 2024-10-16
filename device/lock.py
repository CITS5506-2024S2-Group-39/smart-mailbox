import RPi.GPIO as GPIO
from config import LockConfig
from shared import TimedValue


# Store the password in a file
# For simplicity, store it as plain text without encryption
def set_password(password):
    with open(LockConfig.PASSWORD_FILE, "w") as file:
        file.write(password)


# Get the password from the file
def get_password():
    try:
        with open(LockConfig.PASSWORD_FILE, "r") as file:
            password = file.read().strip()
            return password
    except:
        print("Cannot read the password file.")
        return LockConfig.DEFAULT_PASSWORD  # Default Password


# How much consecutive failures within a timeframe
errorlevel = TimedValue(0)


# Verify the input password by comparing its hash to the stored hash
def verify_password(input_password):
    stored_password = get_password()

    # If password match, return True and clear errorlevel
    if input_password == stored_password:
        errorlevel.clear()
        return True

    # If password does not match, increase errorlevel
    # Too much failure within a short time will result in a high errorlevel
    level = errorlevel.get()
    errorlevel.set(level + 1)
    return False


# Should raise alert or not
def need_raise_alert(threshold):
    level = errorlevel.get()
    if level < threshold:
        return False
    # Clear error level after reporting alert
    # So it will only report if it reaches threshold again later
    errorlevel.clear()
    return True


# Closes the solenoid lock
def lock_close():
    print("Closing lock")
    GPIO.output(LockConfig.RELAY_PIN, GPIO.HIGH)


# Opens the solenoid lock
def lock_open():
    print("Opening lock")
    GPIO.output(LockConfig.RELAY_PIN, GPIO.LOW)


# Checks if the solenoid lock is currently locked
def is_locked():
    return GPIO.input(LockConfig.RELAY_PIN) == GPIO.HIGH


# Set up GPIO for solenoid lock
def init():
    GPIO.setup(LockConfig.RELAY_PIN, GPIO.OUT)
    lock_close()
