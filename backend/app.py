# app.py
from flask import Flask

# Import the blueprints
from events import events_bp
from settings import settings_bp

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(events_bp)
app.register_blueprint(settings_bp)

if __name__ == '__main__':
    app.run(debug=True)
