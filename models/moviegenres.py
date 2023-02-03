from sqlalchemy import Column, ForeignKey, Integer, String
#from sqlalchemy.orm import relationship

from config.database import Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class MovieGenres(Base):

    __tablename__ = "movie_genres"

    mov_id = Column(Integer,primary_key = True)
    gen_id = Column(Integer, ForeignKey("gen.id"))
