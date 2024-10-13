from flask import Flask, request, jsonify
import json
from utils import save_to_db, get_from_db

app = Flask(__name__)

# Endpoint to get all events
@app.route('/api/events', methods=['GET'])
def get_events():
    events = get_from_db("SELECT * FROM events")
    return jsonify(events)

# Endpoint to get or edit a specific event by ID
@app.route('/api/event/<int:event_id>', methods=['GET', 'POST'])
def event_detail(event_id):
    if request.method == 'GET':
        event = get_from_db("SELECT * FROM events WHERE id=?", (event_id,))
        return jsonify(event)
    elif request.method == 'POST':
        data = request.get_json()
        save_to_db("UPDATE events SET data=? WHERE id=?", (json.dumps(data), event_id))
        return jsonify({"message": "Event updated successfully"})

# Endpoint to add a new event
@app.route('/api/event', methods=['PUT'])
def add_event():
    data = request.get_json()
    save_to_db("INSERT INTO events (time, type, data) VALUES (?, ?, ?)",
               (data['time'], data['type'], json.dumps(data['data'])))
    return jsonify({"message": "Event added successfully"})

if __name__ == '__main__':
    app.run(debug=True)
