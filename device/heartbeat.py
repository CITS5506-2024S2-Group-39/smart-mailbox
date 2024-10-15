import requests
import threading
import time
from config import HeartbeatConfig
import lock  # Required to query current lock state
from shared import EventType


def daemon(interrupt, message_queue):
    print("Heartbeat thread started")

    while not interrupt.is_set():
        time.sleep(HeartbeatConfig.INTERVAL)
        try:
            # Heartbeat reports device data to the backend
            # Currently, only report current lock state
            data = {"locked": lock.is_locked()}
            response = requests.post(HeartbeatConfig.URL, json=data)
            response.raise_for_status()
            # Heartbeat also polls commands from the backend
            response = response.json()
            # Handle remote password change
            if "password" in response:
                # Expect password reset
                message_queue.put(
                    (EventType.MailboxPasswordChanged, response["password"])
                )
            # Handle remote lock control
            if "locked" in response:
                if response["locked"]:
                    # Expect lock
                    message_queue.put((EventType.MailboxLocked, None))
                else:
                    # Expect unlock
                    message_queue.put((EventType.MailboxUnlocked, None))
        except Exception as e:
            print("Heartbeat error:", e)

    print("Heartbeat thread stopped")


def init(interrupt, message_queue):
    # Start the heartbeat thread
    thread = threading.Thread(target=daemon, args=(interrupt, message_queue))
    thread.start()
