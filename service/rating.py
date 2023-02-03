from models.rating import Rating as ratingModel

class RatingService():
    def __init__(self,db) -> None:
        self.db = db

    def get_rating(self) -> ratingModel:
        result = self.db.query(ratingModel).all()
        return result

    def create_rating(self,rating:ratingModel):
        new_rating = ratingModel(
        rev_id = rating.rev_id,
        mov_id = rating.mov_id,
        rev_stars = rating.rev_stars,
        num_o_ratings = rating.num_o_ratings
        )
        self.db.add(new_rating)
        self.db.commit()
        return
