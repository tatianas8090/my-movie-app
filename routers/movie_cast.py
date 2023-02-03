from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder


from config.database import Session
from schemas.movie_cast import MovieCast
from models.moviecast import MovieCast as MovieCastModel
from service.movie_cast import MovieCastService


movie_cast_router = APIRouter()


@movie_cast_router.get('/movie/{id_movie}/cast/', tags=['cast'],status_code=200)
def get_movie_cast(id_movie:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieCastService(db).get_movie_cast(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_cast_router.post('/cast', tags=['cast'],response_model=dict,status_code=201)
def create_movie_cast(cast:MovieCast)->dict:
    db = Session()
    MovieCastService(db).create_movie_cast(cast)
    return JSONResponse(content={"message":"Se ha registrado el cast Movie","status_code":201})

@movie_cast_router.put('/cast{id}',tags=['cast'])
def update_cast(id:int,cast:MovieCast):
    db =  Session
    result = MovieCastService(db).get_movie_cast(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    MovieCastService(db).update_cast(id,cast)
    return JSONResponse(content={"message":"Se ha modificado el movie cast con id: {id}"})

@movie_cast_router.delete('/cast/{id}',tags=['cast'])
def delete_movie_cast(id:int):
        db = Session()
        result = MovieCastService(db).get_movie_cast()
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        MovieCastService(db).delete_movie_cast(id)
        return JSONResponse(content="Delete movie cast", status_code=200)