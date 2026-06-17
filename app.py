import os
from flask import Flask, jsonify

app = Flask(__name__)

# Reads from Azure App Service Application Settings (environment variables).
# This demonstrates configuring the app without changing code (Task 4).
APP_MESSAGE = os.environ.get("APP_MESSAGE", "Hello from Azure App Service! (default message)")
APP_ENVIRONMENT = os.environ.get("APP_ENVIRONMENT", "not-set")


@app.route("/")
def home():
    return f"""
    <html>
        <head><title>Azure App Service Demo</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 80px;">
            <h1>{APP_MESSAGE}</h1>
            <p>This is a Python (Flask) web app deployed to Azure App Service.</p>
            <p>Current environment setting: <strong>{APP_ENVIRONMENT}</strong></p>
            <p><a href="/health">Health check</a></p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="ok", message=APP_MESSAGE, environment=APP_ENVIRONMENT)


if __name__ == "__main__":
    # Used only for local testing; Azure App Service runs this via gunicorn instead.
    app.run(host="0.0.0.0", port=8000, debug=True)
