from typing import Optional
from pydantic import BaseModel, Field



class Rating(BaseModel):
        rev_id: int
        mov_id: int
        rev_stars: float
        num_o_ratings: int

        class Config:
            schema_extra = {
                "example":{
                    "rev_id": 1,
                    "mov_id": 1,
                    "rev_stars" : 8.4,
                    "num_o_ratings": 100
                }
            }