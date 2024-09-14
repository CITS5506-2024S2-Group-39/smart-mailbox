import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

P1 = 4
P2 = 3
P3 = 2
P4 = 18
P5 = 17
P6 = 15
P7 = 14

GPIO.setup(P1, GPIO.OUT)
GPIO.setup(P2, GPIO.OUT)
GPIO.setup(P3, GPIO.OUT)

GPIO.setup(P4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(P5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(P6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(P7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

KEY = {
    (18, 4): '1',
    (18, 3): '2',
    (18, 2): '3',
    (17, 4): '4',
    (17, 3): '5',
    (17, 2): '6',
    (15, 4): '7',
    (15, 3): '8',
    (15, 2): '9',
    (14, 4): '*',
    (14, 3): '0',
    (14, 2): '#',
}

last = None


def scan():
    global last
    keys = []

    for col in [P1, P2, P3]:
        GPIO.output(col, GPIO.HIGH)
        for row in [P4, P5, P6, P7]:
            if GPIO.input(row):
                key = KEY[(row, col)]
                keys.append(key)
        GPIO.output(col, GPIO.LOW)

    if len(keys) != 1:
        last = None
        return None

    key, = keys
    if last == key:
        return None

    last = key
    return key


while True:
    result = scan()
    if result:
        key = result
        print(key)
    time.sleep(0.1)
