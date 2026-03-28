from flask import Flask
import requests
import json

app = Flask(__name__)

USERS_API = "http://internal-alb-dns/users"
PAYMENTS_API = "http://internal-alb-dns/payments"


@app.route("/")
def home():

    try:
        users_response = requests.get(USERS_API)
        users_data = users_response.json()

        payments_response = requests.get(PAYMENTS_API)
        payments_data = payments_response.json()

    except Exception as e:
        return f"Error contacting microservices: {e}"

    users_list = ""
    for user in users_data["users"]:
        users_list += f"<li>{user}</li>"

    payments_list = ""
    for payment in payments_data["payments"]:
        payments_list += f"<li>ID {payment['id']} Amount {payment['amount']}</li>"

    html = f"""
    <h1>Enterprise Microservices Demo</h1>

    <h2>Users Service ({users_data['server']})</h2>
    <ul>
    {users_list}
    </ul>

    <h2>Payments Service ({payments_data['server']})</h2>
    <ul>
    {payments_list}
    </ul>
    """

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)