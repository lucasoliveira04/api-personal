from flask import Flask
from controllers.profile_controller import profile_controller
from services.supabase import get_connection

app = Flask(__name__)

PREFIX = "/api/v1"

app.register_blueprint(profile_controller, url_prefix=PREFIX)

if __name__ == "__main__":
    if get_connection():
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("Failed to connect to the database. Please check your connection settings.")
        exit(1)