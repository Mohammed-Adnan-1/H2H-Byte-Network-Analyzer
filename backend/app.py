from flask import Flask
from flask_cors import CORS
from backend.routes import register_routes

#  First create app
app = Flask(__name__)

#  Then apply CORS
CORS(app)

#  Then register routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)