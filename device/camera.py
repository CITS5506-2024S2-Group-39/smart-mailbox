import base64
import io
import threading
import time
from picamera2 import Picamera2
import RPi.GPIO as GPIO
from config import CameraConfig
from shared import EventType


# Thread to continuously monitor for mail detection
def daemon(interrupt, message_queue):
    camera = Picamera2()
    camera.start()
    print("Mailbox monitoring thread started")

    while not interrupt.is_set():
        time.sleep(1)

        # Check if the break beam sensor is not interrupted (no mail detected)
        if GPIO.input(CameraConfig.SENSOR_PIN) == GPIO.HIGH:
            continue

        # Mail detected: turn on the LED
        print("Mail detected")
        GPIO.output(CameraConfig.LED_PIN, GPIO.HIGH)

        # Wait until the mail has fully entered the mailbox
        while GPIO.input(CameraConfig.SENSOR_PIN) == GPIO.LOW:
            time.sleep(1)

        # Capture an image of the mail
        print("Capturing image...")
        file = io.BytesIO()
        camera.capture_file(file, format="jpeg")
        file.seek(0)
        rawbytes = file.read()  # Binary data
        b64bytes = base64.b64encode(rawbytes)
        b64string = b64bytes.decode("utf-8")

        # Turn off the LED after capturing the image
        GPIO.output(CameraConfig.LED_PIN, GPIO.LOW)

        # Create an event and add it to the message queue for processing
        message_queue.put((EventType.MailboxIncomingMail, b64string))

    camera.stop()
    print("Mailbox monitoring thread stopped")


def init(interrupt, message_queue):
    # Configure the GPIO pins for the sensor and LED
    GPIO.setup(CameraConfig.SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(CameraConfig.LED_PIN, GPIO.OUT)

    # Start the mailbox monitoring thread
    thread = threading.Thread(target=daemon, args=(interrupt, message_queue))
    thread.start()
