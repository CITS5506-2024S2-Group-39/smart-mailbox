from flask import Blueprint, request, jsonify
from utils import save_to_db, get_from_db
from shared import ISODateTime

# Define a Blueprint for device management related endpoints
device_management_bp = Blueprint("device_management", __name__)

class DeviceManagementContext:
    def __init__(self):
        # Device lock status, reported by the device itself
        self.locked = True
        # Timestamp for when the device first came online
        self.since = ISODateTime(1970, 1, 1)
        # Timestamp for when the device last checked in
        self.lastseen = ISODateTime(1970, 1, 1)
        # Dictionary to store commands queued for the device
        self.expect = {}

    def is_online(self):
        # Determine if the device is considered online based on the last seen time
        now = ISODateTime.now()
        lastseen = self.lastseen
        # If the device has not been seen for over 60 seconds, it's considered offline
        return (now - lastseen).total_seconds() < 60

    def get_expected_state(self):
        # Retrieve and clear the queued commands for the device
        expect = self.expect
        self.expect = {}
        return expect

# Context object for managing the state of a single device
context = DeviceManagementContext()

# Endpoint for the device to report its status and receive queued commands
@device_management_bp.route("/api/mailbox/heartbeat", methods=["POST"])
def get_commands():
    # Parse the status report sent by the device
    data = request.get_json()
    context.locked = data["locked"]

    # Update timestamps based on device check-in status
    now = ISODateTime.now()
    if not context.is_online():
        context.since = now
    context.lastseen = now

    # Send back any queued commands for the device
    expect = context.expect
    context.expect = {}
    return jsonify(expect)

# Endpoint to lock or unlock the mailbox
@device_management_bp.route("/api/mailbox/lock", methods=["POST"])
def lock_mailbox():
    # Receive the lock command from the request
    data = request.get_json()
    locked = data["locked"]
    # Queue the lock/unlock command for the device
    context.expect["locked"] = locked
    return jsonify({})

# Endpoint to reset the device password
@device_management_bp.route("/api/mailbox/reset", methods=["POST"])
def change_password():
    # Parse the new password from the request
    data = request.get_json()
    password = data["password"]
    
    # Validate that the password is a string of digits
    if not isinstance(password, str):
        raise Exception("Password must be a string")

    if not 6 <= len(password):
        raise Exception("Password must be at least 6 characters long")

    for digit in password:
        if digit not in "0123456789":
            raise Exception("Password must contain only digits 0-9")
    
    # Queue the password change command for the device
    context.expect["password"] = password
    return jsonify({})

# Endpoint for the frontend to check the current status of the device
@device_management_bp.route("/api/devstat", methods=["GET"])
def get_device_status():
    # Return the online status, connection timestamps, and lock status
    return jsonify(
        {
            "online": context.is_online(),
            "since": str(context.since),
            "lastseen": str(context.lastseen),
            "locked": context.locked,
        }
    )
