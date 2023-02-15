# IMPORTING REQUIRED PACKAGES
import requests
from flask import Flask, request, jsonify

# CREATE FLASK APP
app = Flask(__name__)


# HELPER FUNCTION TO CHECK REQUEST BODY CONTENT TYPE
def check_content_type(incoming_request):
    status = False
    content_type = incoming_request.headers.get("Content-Type")
    if content_type == "application/json":
        status = True
    return status


# MAKE GET REQUEST
def make_GET_request(port, service):
    url = "http://127.0.0.1:port/service".replace("port", port).replace("service", service)
    return requests.get(url)


# MAKE POST REQUEST
def make_POST_request(port, service, payload):
    url = "http://127.0.0.1:port/service".replace("port", port).replace("service", service)
    return requests.post(url=url, json=payload)


# HANDLE INCOMING REQUEST
@app.route("/db-app", methods=["GET", "POST"])
def handle_app_requests():
    # HANDLE ALL GET REQUESTS
    if request.method == "GET":
        return jsonify({"supported functions": "get data", "supported DB": "MySQL, MongoDB"})

    # HANDLE ALL POST REQUESTS
    if request.method == "POST":
        if check_content_type(request):
            request_body = request.json
            if "type" in request_body.keys():
                if request_body["type"].upper() == "SQL":
                    response = make_POST_request("5001", "get-data", request_body)
                    return response.json()
                if request_body["type"].upper() == "MONGODB":
                    response = make_POST_request("5002", "get-data", request_body)
                    return response.json()
        return jsonify({"error": "Content-Type not supported!"})


# RUN FLASK APP
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)