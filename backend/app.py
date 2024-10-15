########################################################################

# Enable importing `shared` from the parent directory
import sys, os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

########################################################################


from flask import Flask, jsonify

# Import the blueprints
from events import events_bp
from settings import settings_bp
from device_management import device_management_bp

app = Flask(__name__)

# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    response = { "error": str(e) }
    return jsonify(response), 500

# Register the blueprints
app.register_blueprint(events_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(device_management_bp)

if __name__ == '__main__':
    app.run(debug=True)
