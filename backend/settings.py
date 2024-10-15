# settings.py
from flask import Blueprint, request, jsonify
import json
from utils import save_to_db, get_from_db

settings_bp = Blueprint('settings', __name__)

# Endpoint to get all settings
@settings_bp.route('/api/settings', methods=['GET'])
def get_settings():
    settings = get_from_db("SELECT * FROM settings")
    return jsonify(settings)

# Endpoint to update or create new settings
@settings_bp.route('/api/settings', methods=['POST'])
def update_settings():
    data = request.get_json()
    for setting in data:
        save_to_db("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
                   (setting['key'], setting['value']))
    return jsonify({})
