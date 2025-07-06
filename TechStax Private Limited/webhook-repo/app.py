from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from models import format_document
from datetime import datetime
import utils

app = Flask(__name__)

# Replace with your MongoDB URI
client = MongoClient("mongodb://localhost:27017/")
db = client["github_events"]
collection = db["events"]

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    action_type = request.headers.get('X-GitHub-Event')

    if action_type == "push":
        data = {
            "request_id": payload['after'],
            "author": payload['pusher']['name'],
            "action": "PUSH",
            "from_branch": None,
            "to_branch": payload['ref'].split('/')[-1],
            "timestamp": datetime.utcnow().isoformat()
        }
        collection.insert_one(data)

    elif action_type == "pull_request":
        action = payload['action']
        if action == "opened":
            pr = payload['pull_request']
            data = {
                "request_id": str(pr['id']),
                "author": pr['user']['login'],
                "action": "PULL_REQUEST",
                "from_branch": pr['head']['ref'],
                "to_branch": pr['base']['ref'],
                "timestamp": datetime.utcnow().isoformat()
            }
            collection.insert_one(data)

    elif action_type == "merge":
        # Optional: Only if you use a custom hook to track merges
        pass

    return jsonify({"status": "received"}), 200

@app.route('/')
def index():
    docs = collection.find().sort("timestamp", -1).limit(10)
    formatted_docs = [format_document(doc) for doc in docs]
    return render_template('index.html', records=formatted_docs)

@app.route('/poll')
def poll():
    docs = collection.find().sort("timestamp", -1).limit(10)
    formatted_docs = [format_document(doc) for doc in docs]
    return jsonify(formatted_docs)
