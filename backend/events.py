from flask import Blueprint, request, jsonify, send_from_directory
from base64 import b64decode
from hashlib import sha256
from os.path import join

from utils import get_events_from_db, get_events_after_id_from_db
from utils import get_event_from_db, update_event_to_db
from config import IMAGE_FOLDER
from utils import save_event_to_db, get_setting_item
from gpt import make_prompt, analyze_mail_cover
from notification import send_email_notification
from shared import EventType


events_bp = Blueprint("events", __name__)


# Endpoint to get all events
@events_bp.route("/api/events", methods=["GET"])
def get_events():
    events = get_events_from_db()
    return jsonify(events)


# Endpoint to get events after the specified id
@events_bp.route("/api/events", methods=["POST"])
def get_events_delta():
    data = request.get_json()
    id = data['id']
    events = get_events_after_id_from_db(id)
    return jsonify(events)

# Endpoint to get a specific event by ID
@events_bp.route("/api/event/<int:id>", methods=["GET"])
def get_event(id: int):
    event = get_event_from_db(id)
    return jsonify(event)


# Endpoint to edit a specific event by ID
@events_bp.route("/api/event/<int:id>", methods=["POST"])
def update_event(id: int):
    data = request.get_json()
    update_event_to_db(id, data)
    return jsonify({})


# Serve the uploaded files
@events_bp.route("/api/images/<filename>")
def uploaded_file(filename):
    return send_from_directory(IMAGE_FOLDER, filename)


def process_normal_event(type: str, time: str, summary: str):
    data = {"summary": summary}
    return (type, time, data)


def process_email_event(type: str, time: str, imageb64: str):
    # Write image to a folder
    content = b64decode(imageb64)
    filename = sha256(content).hexdigest() + ".jpg"
    filepath = join(IMAGE_FOLDER, filename)
    with open(filepath, "wb") as f:
        f.write(content)

    # Construct prompt based on user settings
    region = get_setting_item("prompt.region", "Not Provided")
    address = get_setting_item("prompt.address", "Not Provided")
    users = get_setting_item("prompt.users", "Not Provided")
    comments = get_setting_item("prompt.comments", "Not Provided")
    prompt = make_prompt(region, address, users, comments)

    # Analyze using ChatGPT
    data = analyze_mail_cover(prompt, filepath)
    # Add filename to data for frontend display
    data["image"] = filename
    return (type, time, data)


# Endpoint to add a new event
@events_bp.route("/api/event", methods=["PUT"])
def add_event():
    data = request.get_json()
    type = data["type"]
    time = data["time"]
    data = data["data"]
    if type != EventType.MailboxIncomingMail:
        (type, time, data) = process_normal_event(type, time, data)
    else:
        (type, time, data) = process_email_event(type, time, data)
    id = save_event_to_db(type, time, data)
    send_email_notification(type, time, data, id)
    return jsonify({})
