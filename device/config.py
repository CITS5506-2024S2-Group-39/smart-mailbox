# Make sure to change this value depending on how your backend is hosted
BACKEND_HOST_NAME = "localhost:5000"


# Configuration class for heartbeat settings
class HeartbeatConfig:
    # URL endpoint for the heartbeat API
    URL = f"http://{BACKEND_HOST_NAME}/api/mailbox/heartbeat"


# Configuration class for event reporting settings
class EventReportConfig:
    # URL endpoint for the event reporting API
    URL = f"http://{BACKEND_HOST_NAME}/api/event"
    # Time interval (in seconds) to wait before retrying the event report
    RETRY_INTERVAL = 5
    # Maximum number of retry attempts for event reporting
    MAX_RETRY = 100


# Configuration class for lock settings
class LockConfig:
    # GPIO pin number connected to the relay controlling the solenoid lock
    RELAY_PIN = 26
    # File path where the lock password will be stored
    PASSWORD_FILE = "password.txt"
    # Default password to use if PASSWORD_FILE cannot be read
    DEFAULT_PASSWORD = "55062024"


# Configuration class for camera settings
class CameraConfig:
    # GPIO pin connected to the break beam sensor for the camera
    SENSOR_PIN = 25
    # GPIO pin connected to the LED light for the camera
    LED_PIN = 23


# Configuration class for numpad GPIO pin mappings
class NumPadConfig:
    # GPIO pin mappings for the columns of the numpad
    COL1 = 4
    COL2 = 3
    COL3 = 2
    # GPIO pin mappings for the rows of the numpad
    ROW1 = 18
    ROW2 = 17
    ROW3 = 15
    ROW4 = 14
