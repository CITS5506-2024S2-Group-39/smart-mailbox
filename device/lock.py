import RPi.GPIO as GPIO
import time
import config
import touchpad 
import backend.password_manager

# Set up GPIO for solenoid lock
def setup_lock():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.Config.RELAY_PIN, GPIO.OUT)
    print("Lock set up done")  # for debugging 


#Closes the solenoid lock.
def lock_close():
    print("Locking mailbox...")
    GPIO.output(config.Config.RELAY_PIN, GPIO.HIGH)

#Opens the solenoid lock.
def lock_open():
    print("Unlocking mailbox...")
    GPIO.output(config.Config.RELAY_PIN, GPIO.LOW)

#Handles locking/unlocking based on the correct password.
def handle_lock(input_password):
    stored_password = backend.password_manager.load_password()    # Load the stored (hashed) password from file
    if stored_password is None:
        print("No password found.") # =ppassword file empty 
        touchpad.set_new_pin()
    
    # Verify the input password 
    if backend.password_manager.verify_password(input_password):
        lock_open()
        print("Mailbox unlocked")
        time.sleep(5)  # Keep the lock open for 5 seconds

        lock_close()
        print("Mailbox locked")
    else:
        print("Incorrect password.")