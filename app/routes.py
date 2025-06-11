from flask import request, jsonify,Blueprint
from .db import get_db_connection


main = Blueprint('main', __name__)
from flask import Blueprint

@main.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    username = data.get('name')
    email = data.get('email')

    try:
        conn,cursor = get_db_connection()

        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(query, (username, email))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'User added successfully!'})
    except Exception as e:
        print("Database Error:", e)
        return jsonify({'error': 'Database connection failed'}), 500
    
@main.route('/users', methods=['GET'])
def get_users():
    try:
        conn, cursor = get_db_connection()
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        cursor.close()
        conn.close()

        user_list = [{'name': user[0], 'email': user[1]} for user in users]
        return jsonify(user_list)
    except Exception as e:
        print("Database Error:", e)
        return jsonify({'error': 'Database connection failed'}), 500
