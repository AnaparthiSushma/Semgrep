import os
import subprocess
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Vulnerable to SQL Injection
@app.route('/get_user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return jsonify(user)

# Vulnerable to Command Injection
@app.route('/run_command', methods=['POST'])
def run_command():
    command = request.form['command']
    result = subprocess.check_output(command, shell=True)
    return jsonify({'output': result.decode('utf-8')})

# Vulnerable to Insecure File Handling
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join('/uploads', file.filename))
    return jsonify({'message': 'File uploaded successfully'})

if __name__ == '__main__':
    app.run(debug=True)
