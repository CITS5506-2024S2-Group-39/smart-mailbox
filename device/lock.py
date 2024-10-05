import time
import RPi.GPIO as GPIO

# Set GPIO pin for the break beam sensor
RELAY_PIN = 26  # Adjust according to your wiring

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)


def lock_close():
    print("Closing Lock")
    GPIO.output(RELAY_PIN, GPIO.HIGH)


def lock_open():
    print("Opening Lock")
    GPIO.output(RELAY_PIN, GPIO.LOW)


try:
    while True:
        command = input()
        if command == "open":
            lock_open()
        elif command == "close":
            lock_close()
        time.sleep(2)
except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()  # Clean up GPIO settings
