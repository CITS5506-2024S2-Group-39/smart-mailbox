class HeartbeatConfig:
    INTERVAL = 1
    URL = "http://13.239.34.106/api/mailbox/heartbeat"


class EventReportConfig:
    URL = "http://13.239.34.106/api/event"
    RETRY_INTERVAL = 5
    MAX_RETRY = 100


class LockConfig:
    RELAY_PIN = 26  # Pin of the relay to control the solenoid lock
    PASSWORD_FILE = "password.txt"  # Where the password will be stored
    DEFAULT_PASSWORD = "55062024"  # Default password if PASSWORD_FILE cannot be read


class CameraConfig:
    SENSOR_PIN = 25  # Pin connected to the break beam sensor
    LED_PIN = 23  # Pin connected to the LED light


# Define GPIO pin mappings for the numpad
class NumPadConfig:
    COL1 = 4
    COL2 = 3
    COL3 = 2
    ROW1 = 18
    ROW2 = 17
    ROW3 = 15
    ROW4 = 14
