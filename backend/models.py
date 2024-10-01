from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class MailEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=False)
    image_data = db.Column(db.LargeBinary)
    event_time = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(500))  # Recognition result description
