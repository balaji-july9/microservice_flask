# from services import root_dir, nice_json
from flask import Flask
import json
from werkzeug.exceptions import NotFound


app = Flask(__name__)

with open("../database/bookings.json", "r") as f:
    bookings = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return {
        "uri": "/",
        "subresource_uris": {
            "bookings": "/bookings",
            "booking": "/bookings/<username>"
        }
    }


@app.route("/bookings", methods=['GET'])
def booking_list():
    return bookings


@app.route("/bookings/<username>", methods=['GET'])
def booking_record(username):
    if username not in bookings:
        raise NotFound

    return bookings[username]

if __name__ == "__main__":
    app.run(port=5003, debug=True)

