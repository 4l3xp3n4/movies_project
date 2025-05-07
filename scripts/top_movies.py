import sys
from movies.utils.csv_load import import_movies_from_csv
from movies.utils.movie_utils import top_certified_fresh_movies


def main():
    movies = import_movies_from_csv("../movies.csv")
    top_ten_fresh_movies = top_certified_fresh_movies(movies)
    print(top_ten_fresh_movies)


if __name__ == "__main__":
    main()
    sys.exit()
