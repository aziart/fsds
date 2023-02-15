# IMPORTING REQUIRED PACKAGES
import pymongo
from flask import Flask, request, jsonify

# CREATE FLASK APP
app = Flask(__name__)


# HELPER FUNCTION TO VALIDATE INCOMING REQUEST BODY
def validate_request_body(required_keys, actual_keys):
    status = True
    for key in required_keys:
        if key not in actual_keys:
            status = False
    return status


@app.route("/get-data", methods=["POST"])
def get_data():
    # GET REQUEST BODY
    request_body = request.json

    # CREATE MONGODB CLIENT
    if validate_request_body(["connection-string", "db-name", "collection"], request_body.keys()):
        client = pymongo.MongoClient(str(request_body["connection-string"]))
        db = client[request_body["db-name"]]
        collection = db[request_body["collection"]]
        return jsonify({"data": str(list(collection.find()))})
    return jsonify({"error": "db-name or collection or connection-string not found"})


# RUN FLASK APP
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)