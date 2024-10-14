import config 
import camera
import lock 
import touchpad
import RPi.GPIO as GPIO


def main():
    try:
        GPIO.setmode(GPIO.BCM)
        # Start the camera and touchpad threads
        touchpad.init()  
        camera.init() 
        
        lock.setup_lock()  # Initialize the lock mechanism

        # Main event loop
        while not config.interrupt.is_set():
            event = config.message_queue.get()  # Block until an event is in the queue
            print(f"Got event: type {event.type}, data {event.data}")
            
            # Process different event types
            if event.type == "mail": 
                print(f"Handling mail detection event: {event.data}")
                camera.send_image_to_backend(event.data)  # Process the captured image

            elif event.type == "touchpad_pin":
                print(f"Handling touchpad input event: {event.data}")
                if lock.handle_lock(event.data):  # Handle the lock
                    print("Mailbox access granted.")
                else:
                    print("Access denied.") 

            elif event.type == "touchpad_reset":  # Reset PIN request
                print("Resetting PIN...")
                touchpad.reset_pin()  # Handles the process to reset the PIN

    except KeyboardInterrupt:
        config.interrupt.set()

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()