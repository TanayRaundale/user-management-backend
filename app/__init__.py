from flask import Flask, g
from flask_cors import CORS
from .db import get_db_connection
from .routes import main

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.before_request
    def before_request():
        try:
            conn, cursor = get_db_connection()
            g.db_conn = conn
            g.db_cursor = cursor
        except Exception as e:
            print("❌ Failed to connect to DB during request:", e)

    @app.teardown_request
    def teardown_request(exception=None):
        db_conn = getattr(g, 'db_conn', None)
        if db_conn is not None:
            db_conn.close()

    app.register_blueprint(main)
    return app

