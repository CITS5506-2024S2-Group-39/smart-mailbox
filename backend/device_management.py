from flask import Blueprint, request, jsonify
import json
from utils import save_to_db, get_from_db
import event_types


from datetime import datetime, timezone

device_management_bp = Blueprint('device_management', __name__)

class DeviceManagementContext:
    def __init__(self):
        # Data reported by device
        self.locked = True # is locked or not
        # Data derived from device report
        self.since = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)  # First time device is online
        self.lastseen = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)  # Last time device polled for commands
        # Queued device commands
        self.queuedPassword = None   # Next password
        self.queuedLockState = None  # True for lock, False for unlock

    def is_online(self):
        # If lastseen is too early, then device is considered offline
        now = datetime.now(timezone.utc)
        lastseen = self.lastseen
        return (now - lastseen).seconds < 60

    def get_commands(self):
        password = self.queuedPassword
        self.queuedPassword = None
        lockstate = self.queuedLockState
        self.queuedLockState = None
        commands = []
        if password is not None:
            commands.append({
                "type": event_types.MailboxPasswordChanged,
                "data": password
            })
        if lockstate is not None:
            if lockstate:
                commands.append({
                    "type": event_types.MailboxLocked,
                })
            else:
                commands.append({
                    "type": event_types.MailboxUnlocked,
                })
        return commands

# Currently, only supports a single device
# So we only need 1 context
context = DeviceManagementContext()


# Endpoint to get all commands (for device)
@device_management_bp.route('/api/mailbox/heartbeat', methods=['POST'])
def get_commands():
    # Accept data report
    data = request.get_json()
    context.locked = data['locked']
    # Modify timestamp
    now = datetime.now(timezone.utc)
    if not context.is_online():
        context.since = now
    context.lastseen = now
    # Return queued commands
    response = context.get_commands()
    return jsonify(response)


# Endpoint to lock/unlock mailbox
@device_management_bp.route('/api/mailbox/lock', methods=['POST'])
def lock_mailbox():
    data = request.get_json()
    action = data['action']
    if action == 'unlock':
        context.queuedLockState = False
    else:
        context.queuedLockState = True
    return jsonify({})

# Endpoint to change password
@device_management_bp.route('/api/mailbox/reset', methods=['POST'])
def change_password():
    data = request.get_json()
    password = data['password']
    if not isinstance(password, str):
        raise Exception("Password must be a string")
    for digit in password:
        if digit not in '0123456789':
            raise Exception("Password must contain only digits 0-9")
    context.queuedPassword = password
    return jsonify({})

# Endpoint to get device status (for frontend)
@device_management_bp.route('/api/devstat', methods=['GET'])
def get_device_status():
    return jsonify({
        "online": context.is_online(),
        "since": context.since.isoformat(),
        "lastseen": context.lastseen.isoformat(),
        "locked": context.locked,
    })
