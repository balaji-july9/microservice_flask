# from services import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open("../database/movies.json", "r") as f:
    movies = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return {
        "uri": "/",
        "subresource_uris": {
            "movies": "/movies",
            "movie": "/movies/<id>"
        }
    }

@app.route("/movies/<movieid>", methods=['GET'])
def movie_info(movieid):
    if movieid not in movies:
        raise NotFound

    result = movies[movieid]
    result["uri"] = "/movies/{}".format(movieid)

    return result


@app.route("/movies", methods=['GET'])
def movie_record():
    return movies


if __name__ == "__main__":
    app.run(port=5001, debug=True)

