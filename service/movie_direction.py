from models.moviedirection import MovieDirection as MovieDirectionModel
from schemas.movie_direction import MovieDirection


class MovieDirectionService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_direction(self,id_movie:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.movie_id == id_movie).all()
        return result

    def create_movie_direction(self,movie_direction: MovieDirectionModel):
        new_direction = MovieDirectionModel(
            dir_id = movie_direction.dir_id,
            mov_id = movie_direction.mov_id,
            
        )
        self.db.add(new_direction)
        self.db.commit()
        return