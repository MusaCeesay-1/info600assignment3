from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (replace this with your actual data)
users = [
    {"id": "1", "name": "John Doe", "department": "IT", "year": 2020},
    {"id": "2", "name": "Jane Smith", "department": "Finance", "year": 2019}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Add more routes for handling POST and DELETE requests here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
