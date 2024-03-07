from flask import Flask, request
from flask_cors import CORS

def before_request():
    print(f"Received request: {request.method} {request.path}")
    if request.method == "POST":
        print(f"Request body: {request.json}")


def after_request(response):
    print(f"Sending response: {response.status_code}")
    return response

def configure_middlewares(app: Flask):
    CORS(app)
    app.before_request(before_request)
    app.after_request(after_request)


