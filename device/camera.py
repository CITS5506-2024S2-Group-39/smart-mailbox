from picamera2 import Picamera2
import time
import RPi.GPIO as GPIO
from config import Config
import requests

# Initialize the camera
camera = picamera2.Picamera2()

def setup_camera():
    #Sets up the GPIO for the sensor and camera
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Config.SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def is_sensor_triggered():
    #Checks if the sensor is triggered (beam interrupted).
    return GPIO.input(Config.SENSOR_PIN) == GPIO.LOW

def capture_image():
    #Captures an image using the Pi Camera.
    print("Capturing image...")
    camera.start()
    time.sleep(2)  
    camera.capture_file(Config.IMAGE_STORAGE_PATH)
    camera.stop()
    print(f"Image saved at {Config.IMAGE_STORAGE_PATH}")

def send_image_to_backend():
    #Sends the captured image to the backend.
    url = Config.API_ENDPOINTS['mail_event']
    files = {'file': open(Config.IMAGE_STORAGE_PATH, 'rb')}
    data = {'device_id': Config.DEVICE_ID}

    try:
        response = requests.post(url, files=files, data=data, timeout=Config.REQUEST_TIMEOUT)
        response.raise_for_status()
        print(f"Image sent to backend successfully: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send image: {e}")