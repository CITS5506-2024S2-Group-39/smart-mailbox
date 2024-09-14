import picamera2
import time
import RPi.GPIO as GPIO

# Set the GPIO pin number for the light sensor
sensor_pin = 17  # Adjust according to the actual pin

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

# Initialize the camera
camera = picamera2.Picamera2()

try:
    print("Waiting for light interruption signal...")
    # Wait for the light interruption signal (assuming high level indicates the signal)
    while GPIO.input(sensor_pin) == 0:
        time.sleep(0.1)  # Polling interval

    print("Light interruption detected, waiting for 1 second...")
    time.sleep(1)  # Wait for 1 second

    # Start the camera and capture a photo
    camera.start()
    time.sleep(2)  # Allow the camera to adjust brightness
    image_path = "Firstpic.jpg"
    camera.capture_file(image_path)
    camera.stop()
    print("Photo taken, image saved at:", image_path)

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
