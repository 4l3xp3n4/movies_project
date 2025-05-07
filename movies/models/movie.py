class Movie:
    def __init__(self, id: str, rating: int, movie_title: str, certified_fresh: bool):
        self.id: str = id
        self.rating: int = rating
        self.movie_title: str = movie_title
        self.certified_fresh: bool = certified_fresh

    def __repr__(self):
        return f"<Movie(id='self.id', rating={self.rating}, movie_title={self.movie_title}, certified_fresh={self.certified_fresh} )>"

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "movie_title": self.movie_title,
            "certified_fresh": self.certified_fresh,
        }
