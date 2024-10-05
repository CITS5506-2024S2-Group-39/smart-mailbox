import time
import RPi.GPIO as GPIO
from picamera2 import Picamera2

# Set GPIO pin for the break beam sensor
BEAM_SENSOR_PIN = 25  # Adjust according to your wiring
LED_LIGHT_PIN = 23
CAMERA_IMAGE_PATH = "mail_image.jpg"

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use pull-up resistor
GPIO.setup(LED_LIGHT_PIN, GPIO.OUT)

# Initialize camera
camera = Picamera2()

if GPIO.input(BEAM_SENSOR_PIN) == GPIO.LOW:
    print("Waiting for beam to be restored...")
    while GPIO.input(BEAM_SENSOR_PIN) == GPIO.LOW:
        time.sleep(0.1)


# Define function to capture image
def capture_image():
    GPIO.output(LED_LIGHT_PIN, GPIO.HIGH)
    camera.start()
    time.sleep(2)  # Warm-up time for camera to stabilize image
    camera.capture_file(CAMERA_IMAGE_PATH)
    camera.stop()
    GPIO.output(LED_LIGHT_PIN, GPIO.LOW)


try:
    print("Waiting for mail...")

    while True:
        # Wait for the beam to be interrupted (LOW indicates beam is broken)
        if GPIO.input(BEAM_SENSOR_PIN) == GPIO.LOW:
            print("Mail detected! Capturing image...")
            capture_image()  # Call function to capture image
            # Wait for the beam to be restored (when the beam returns to HIGH)
            while GPIO.input(BEAM_SENSOR_PIN) == GPIO.LOW:
                time.sleep(0.1)
            print("Beam restored, ready for next detection...")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
