#creating flask server

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Sessions landing page"

@app.route('/sessions', methods=['POST'])
def create_session():
    jsonstring = request.json
    return f'Created session\n{jsonstring}'

@app.route('/sessions', methods=['GET'])
def get_session_all():
    return f'Getting all sessions'

@app.route('/sessions/<int:id>', methods=['GET'])
def get_session_byid(id):
    return f'Your session ID is {id}'

@app.route('/sessions/<int:id>', methods=['PUT'])
def update_session(id):
    jsonstring = request.json
    return f'Your session {id}: {jsonstring}'

@app.route('/sessions/<int:id>', methods=['DELETE'])
def delete_session_byid(id):
    return f'Session {id} is deleted'

if __name__ == "__main__":
    app.run(debug = True)