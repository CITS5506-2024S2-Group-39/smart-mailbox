import threading
import datetime
import time
from picamera2 import Picamera2
import RPi.GPIO as GPIO
import config
import requests

# Initialize the camera
camera = picamera2.Picamera2()

#Sets up the GPIO for the sensor and camera
def setup_camera():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(config.Config.SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.Config.LED_PIN, GPIO.OUT) 
    print("Camera set up is done")  # for debugging 

#Captures an image using the Pi Camera.
def capture_image():
    formatted_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"image-{formatted_time}.jpg"


    GPIO.output(LED_LIGHT_PIN, GPIO.HIGH)  # Turn on LED
    print("Capturing image...")
    camera.start()
    time.sleep(2)  
    camera.capture_file(filename)
    camera.stop()
    GPIO.output(LED_LIGHT_PIN, GPIO.LOW)  # Turn off LED

    print(f"Image saved at {filename}")
    return filename 

# !!!! Still haven't verified this logic!!!
#Sends the captured image to the backend
def send_image_to_backend():
    url = config.Config.API_ENDPOINTS['mail_event']
    files = {'file': open(config.Config.IMAGE_STORAGE_PATH, 'rb')}
    data = {'device_id': config.Config.DEVICE_ID}

    try:
        response = requests.post(url, files=files, data=data, timeout=config.Config.REQUEST_TIMEOUT)
        response.raise_for_status()
        print(f"Image sent to backend successfully: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send image: {e}")

# Thread to monitor mail detection
def daemon():
    print("Mailbox monitoring thread started")

    while not config.interrupt.is_set():
        if GPIO.input(config.Config.SENSOR_PIN) == GPIO.LOW:
            print("Mail detected, capturing image...")
            filename = capture_image()

            # Create an event and add it to the message queue
            event = config.Event(event_type="mail", data=filename)
            config.message_queue.put(event)

        time.sleep(1)  # Polling interval

    print("Mailbox monitoring thread stopped")

# Initialize the thread
def init():
    setup_camera()
    thread = threading.Thread(target=daemon)
    thread.start()