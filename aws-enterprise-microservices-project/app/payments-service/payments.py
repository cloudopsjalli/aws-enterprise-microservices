from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/payments")
def payments():

    hostname = socket.gethostname()

    data = {
        "service": "payments-service",
        "server": hostname,
        "payments": [
            {"id":1,"amount":100},
            {"id":2,"amount":250}
        ]
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)