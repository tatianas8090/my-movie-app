from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MovieDirection(Base):

    __tablename__ = "movie_direction"
    id=Column(Integer,primary_key=True)
    dir_id = Column(Integer, ForeignKey("dir.id"))
    mov_id = Column(Integer, ForeignKey("mov.id"))