import RPi.GPIO as GPIO
import time
import config
import touchpad 
import password_manager



#Closes the solenoid lock.
def lock_close():
    print("Locking mailbox...")
    GPIO.output(config.Config.RELAY_PIN, GPIO.HIGH)

#Opens the solenoid lock.
def lock_open():
    print("Unlocking mailbox...")
    GPIO.output(config.Config.RELAY_PIN, GPIO.LOW)

# Set up GPIO for solenoid lock
def setup_lock():
    GPIO.setup(config.Config.RELAY_PIN, GPIO.OUT)
    lock_close()
    print("Lock set up done")  # for debugging 


#Handles locking/unlocking based on the correct password.
def handle_lock(input_password):
    if not input_password:
        lock_close()
        return

    stored_password = password_manager.load_password()    # Load the stored (hashed) password from file
    if stored_password is None:
        print("No password found.") # =ppassword file empty 
        touchpad.set_new_pin()
    
    # Verify the input password 
    if password_manager.verify_password(input_password):
        lock_open()
        print("Mailbox unlocked")
    else:
        print("Incorrect password.")