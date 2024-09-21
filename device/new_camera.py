import time
import RPi.GPIO as GPIO
from picamera import PiCamera

# Set GPIO pin for the break beam sensor
BEAM_SENSOR_PIN = 17  # Adjust according to your wiring
CAMERA_IMAGE_PATH = '/home/pi/mail_image.jpg'

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use pull-up resistor

# Initialize camera
camera = PiCamera()

# Define function to capture image
def capture_image():
    camera.start_preview()
    time.sleep(2)  # Warm-up time for camera to stabilize image
    camera.capture(CAMERA_IMAGE_PATH)
    camera.stop_preview()

try:
    print("Waiting for mail...")
    
    while True:
        # Wait for the beam to be interrupted (LOW indicates beam is broken)
        if GPIO.input(BEAM_SENSOR_PIN) == GPIO.LOW:
            print("Mail detected! Capturing image...")
            capture_image()  # Call function to capture image
            time.sleep(5)  # Delay after capturing to prevent repeated shots
            
            # Wait for the beam to be restored (when the beam returns to HIGH)
            while GPIO.input(BEAM_SENSOR_PIN) == GPIO.LOW:
                time.sleep(0.1)

            print("Beam restored, ready for next detection...")
            time.sleep(2)  # Short delay to prevent frequent triggering
except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
