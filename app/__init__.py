from flask import Flask
from flask_cors import CORS
from .db import get_db_connection
from .routes import main

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Create a DB connection and attach it to app config
    conn = get_db_connection()
    app.config['DB_CONN'] = conn

    app.register_blueprint(main)

    return app
