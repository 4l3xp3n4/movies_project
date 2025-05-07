from typing import List
from movies.models.movie import Movie


def top_certified_fresh_movies(movies: List[Movie], count=10) -> List[Movie]:
    fresh_movies = [m for m in movies if m.certified_fresh]
    fresh_movies.sort(key=lambda m: m.rating, reverse=True)
    return fresh_movies[:count]
