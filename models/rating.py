from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from config.database import Base
from models.reviewer import Reviewer


class Rating(Base):

    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, index=True)
    mov_id = Column(Integer, ForeignKey("movie.id"))
    rev_id = Column(Integer, ForeignKey("reviewer.rev_id"))
    rev_stars = Column(Float)
    num_o_ratings = Column(Integer)