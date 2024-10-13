from flask import Flask, request, jsonify
import json
from utils import save_to_db, get_from_db

app = Flask(__name__)

# Endpoint to get all settings
@app.route('/api/settings', methods=['GET'])
def get_settings():
    settings = get_from_db("SELECT * FROM settings")
    return jsonify(settings)

# Endpoint to update or create new settings
@app.route('/api/settings', methods=['POST'])
def update_settings():
    data = request.get_json()
    for setting in data:
        save_to_db("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
                   (setting['key'], json.dumps(setting['value'])))
    return jsonify({"message": "Settings updated successfully"})

if __name__ == '__main__':
    app.run(debug=True)
