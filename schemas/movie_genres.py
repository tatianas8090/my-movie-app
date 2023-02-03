from typing import Optional
from pydantic import BaseModel, Field


class MovieGenres(BaseModel):
        mov_id: int = Field(ge=1)
        gen_id: int = Field(ge=1,le=100)
    
      

        class Config:
            schema_extra = {
                "example":{
                    "mov_id": 926,
                    "gen_id": 1009,
                   
                }
            }