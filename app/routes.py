from flask import Flask, jsonify
from movies.utils.csv_load import import_movies_from_csv
from movies.utils.movie_utils import top_certified_fresh_movies

app = Flask(__name__)
movie_list = []


@app.route("/movies/top")
def home():
    top_fresh_movies = [m.to_dict() for m in top_certified_fresh_movies(movie_list)]
    return jsonify({"movies": top_fresh_movies})


def start():
    global movie_list
    movie_list = import_movies_from_csv("./movies.csv")
    app.run(debug=True)


if __name__ == "__main__":
    print("main")
    start()
