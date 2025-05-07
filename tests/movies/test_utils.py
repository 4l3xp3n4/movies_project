import unittest
from movies.models.movie import Movie
from movies.utils.movie_utils import top_certified_fresh_movies


class TestTopCertifiedFreshMovies(unittest.TestCase):
    def setUp(self):
        self.movies = [
            Movie("1", 80, "Movie A", True),
            Movie("2", 95, "Movie B", True),
            Movie("3", 90, "Movie C", True),
            Movie("4", 85, "Movie D", False),  # Not certified fresh
            Movie("5", 70, "Movie E", True),
            Movie("6", 60, "Movie F", True),
        ]

    def test_empty_list_input(self):
        result = top_certified_fresh_movies([])
        self.assertEqual(result, [])

    def test_return_top_n_certified_fresh(self):
        result = top_certified_fresh_movies(self.movies, count=2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].movie_title, "Movie B")
        self.assertEqual(result[1].movie_title, "Movie C")

    def test_excludes_non_certified_fresh(self):
        result = top_certified_fresh_movies(self.movies, len(self.movies))

        for m in result:
            self.assertTrue(m.certified_fresh)


if __name__ == "__main__":
    unittest.main()
