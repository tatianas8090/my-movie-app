from models.moviegenres import MovieGenres as MovieGenresModel
from schemas.movie_genres import MovieGenres


class MovieGenresService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_genres(self,id_movie:int):
        result = self.db.query(MovieGenresModel).filter(MovieGenresModel.movie_id == id_movie).all()
        return result

    def create_genres(self,movie_genres: MovieGenresModel):
        new_genres = MovieGenresModel(
            mov_id = movie_genres.mov_id,
            gen_id = movie_genres.gen_id,
            
        )
        self.db.add(new_genres)
        self.db.commit()
        return