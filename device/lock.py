import RPi.GPIO as GPIO
import time
from config import Config
from touchpad import input_password, verify_password

def setup_lock():
    # Set up GPIO for solenoid lock
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Config.RELAY_PIN, GPIO.OUT)
    lock_close()


def lock_close():
    #Closes the solenoid lock.
    print("Locking mailbox...")
    GPIO.output(Config.RELAY_PIN, GPIO.HIGH)

def lock_open():
    #Opens the solenoid lock.
    print("Unlocking mailbox...")
    GPIO.output(Config.RELAY_PIN, GPIO.LOW)

def handle_lock():
    #Handles locking/unlocking based on the correct password.
    stored_password = "1234"  
    if verify_password(stored_password):
        lock_open()
        print("Mailbox unlocked")
        time.sleep(5)  # Keep the lock open for 5 seconds
        lock_close()
        print("Mailbox locked")
    else:
        print("Incorrect password.")