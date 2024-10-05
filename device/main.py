from camera import setup_camera, is_sensor_triggered, capture_image, send_image_to_backend
from lock import setup_lock, handle_lock
from touchpad import setup_touchpad
import RPi.GPIO as GPIO
import time

def main():
    try:
        # Set up the camera, sensor, solenoid lock, and touchpad
        setup_camera()
        setup_lock()
        setup_touchpad()

        print("Waiting for mail detection...")

        while True:
            if is_sensor_triggered():
                print("Mail detected, capturing image...")
                capture_image()
                send_image_to_backend()
                time.sleep(5)  # Prevent immediate re-triggering

            print("Waiting for user to unlock mailbox...")
            handle_lock()  # Handle locking and unlocking the mailbox with the touchpad
            time.sleep(5)  # Prevent immediate re-triggering

    except KeyboardInterrupt:
        print("Program interrupted")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()