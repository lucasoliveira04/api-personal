from flask import Flask
from controllers.profile_controller import profile_controller


app = Flask(__name__)

PREFIX = "/api/v1"

app.register_blueprint(profile_controller, url_prefix=PREFIX)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)