# from services import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open("../database/showtimes.json", "r") as f:
    showtimes = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return {
        "uri": "/",
        "subresource_uris": {
            "showtimes": "/showtimes",
            "showtime": "/showtimes/<date>"
        }
    }


@app.route("/showtimes", methods=['GET'])
def showtimes_list():
    return showtimes


@app.route("/showtimes/<date>", methods=['GET'])
def showtimes_record(date):
    if date not in showtimes:
        raise NotFound
    print(showtimes[date])
    return showtimes[date]

if __name__ == "__main__":
    app.run(port=5002, debug=True)
