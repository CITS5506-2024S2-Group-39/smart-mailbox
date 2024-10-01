import os
import requests
from flask import Flask, request, jsonify
from models import db, MailEvent
from io import BytesIO

app = Flask(__name__)

# Initialize the database
app.config.from_object('config.Config')
db.init_app(app)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # OpenAI API Key

# Allowed file types
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Send image to OpenAI for recognition
def send_image_to_openai(image_data):
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    files = {
        'file': BytesIO(image_data),
    }
    
    response = requests.post('https://api.openai.com/v1/images/recognition', headers=headers, files=files)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"OpenAI request failed: {response.text}")
        return None

@app.route('/mail-event', methods=['POST'])
def mail_event():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # Read the file as binary
        image_data = file.read()

        # Send the image to OpenAI for recognition
        openai_response = send_image_to_openai(image_data)
        if not openai_response:
            return jsonify({'error': 'OpenAI image recognition failed'}), 500
        
        description = openai_response.get('description', 'Unknown recognition result')
        device_id = request.form.get('device_id')
        
        new_event = MailEvent(device_id=device_id, image_data=image_data, description=description)
        db.session.add(new_event)
        db.session.commit()

        return jsonify({'message': 'Mail event processed', 'description': description}), 200
    
    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True)
