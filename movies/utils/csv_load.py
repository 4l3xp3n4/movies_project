import csv
from movies.models.movie import Movie
from typing import List


def import_movies_from_csv(path) -> List[Movie]:
    movies = []
    with open(path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            movie = Movie(
                id=row["id"],
                rating=float(row["rating"]),
                movie_title=row["movie_title"],
                certified_fresh=row["certified_fresh"].lower() == "true",
            )
            movies.append(movie)

        return movies
