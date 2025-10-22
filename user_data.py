from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

def read_data():
    
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []
    with open(DATA_FILE, 'r') as file:
    
        data = json.load(file)
        return data


def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


@app.route('/users', methods=['GET'])
def get_users():
    users = read_data()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users = read_data()
    
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data.get("name")
    }

    users.append(new_user)
    write_data(users)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
