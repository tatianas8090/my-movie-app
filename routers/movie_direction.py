from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder
from models.moviedirection import MovieDirection

from schemas.movie_direction import MovieDirection
from config.database import Session
from service.movie_direction import MovieDirectionService


movie_direction_router = APIRouter()

@movie_direction_router.get('/moviedirection/{id_movie}/directiondirection/', tags=['moviedirection'],response_model=list[MovieDirection],status_code=200)
def get_movie_direction(id_moviedirection:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieDirectionService(db).get_movie_direction(id_moviedirection)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_direction_router.post('/moviedirection', tags=['moviedirection'],response_model=dict,status_code=201)
def create_movie_direction(moviedirection:MovieDirection)->dict:
    db = Session()
    MovieDirectionService(db).create_movie_direction(moviedirection)
    return JSONResponse(content={"message":"Se ha registrado el actor","status_code":201})


@movie_direction_router.put('/moviedirection{id}',tags=['moviedirection'])
def update_movie_direction(id:int,moviedirection:MovieDirection):
    db =  Session
    result = MovieDirectionService(db).update_movie_direction(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    MovieDirectionService(db).update_movie_direction(id,MovieDirection)
    return JSONResponse(content={"message":"Se ha modificado el movie genre con id: {id}"})


@movie_direction_router.delete('/moviedirection/{id}',tags=['moviedirection'])
def delete_movie_direction(id:int):
        db = Session()
        result = MovieDirectionService(db).get_movie_direction(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})

        MovieDirectionService(db).delete_movie_direction(id)
        return JSONResponse(content="Delete movie direction", status_code=200)