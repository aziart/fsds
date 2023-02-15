# IMPORTING REQUIRED PACKAGES
from flask import Flask, request, jsonify
import mysql.connector as conn

# CREATE FLASK APP
app = Flask(__name__)


@app.route("/get-data", methods=["POST"])
def get_data():
    # GET REQUEST BODY
    request_body = request.json

    # CREATE CURSOR
    if "username" in request_body.keys() and "password" in request_body.keys():
        my_db = conn.connect(host="127.0.0.1", user=str(request_body["username"]),
                             passwd=str(request_body["password"]))
        cursor = my_db.cursor()

        # GET DATA FROM DATABASE
        if "query" in request_body.keys():
            cursor.execute(request_body["query"])
            return jsonify({"data": str(cursor.fetchall())})
    return jsonify({"error": "username or password not found"})


# RUN FLASK APP
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)