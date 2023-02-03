from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder
from models.moviegenres import MovieGenres

from schemas.movie_genres import MovieGenres
from config.database import Session
from service.movie_genres import MovieGenresService


movie_genres_router = APIRouter()

@movie_genres_router.get('/moviegenres/{id_moviegenres}/moviegenres/', tags=['moviegenres'],response_model=list[MovieGenres],status_code=200)
def get_movie_genres(id_movie:int = Path(ge=1,le=2000)):
    db = Session()
    result = MovieGenresService(db).get_movie_genres(id_movie)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_genres_router.post('/moviegenres', tags=['moviegenres'],response_model=dict,status_code=201)
def create_movie_genres(moviegenres:MovieGenres)->dict:
    db = Session()
    MovieGenresService(db).create_movie_genres(moviegenres)
    return JSONResponse(content={"message":"Se ha registrado el actor","status_code":201})



@movie_genres_router.put('/moviegenres{id}',tags=['moviegenres'])
def update_movie_genres(id:int,moviegenres:MovieGenres):
    db =  Session
    result = MovieGenresService(db).update_movie_genres(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    MovieGenresService(db).update_movie_genres(id,MovieGenres)
    return JSONResponse(content={"message":"Se ha modificado el movie genre con id: {id}"})


@movie_genres_router.delete('/moviegenres/{id}',tags=['moviegenres'])
def delete_movie_genres(id:int):
        db = Session()
        result = MovieGenresService(db).get_movie_genres(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})

        MovieGenresService(db).delete_movie_genres(id)
        return JSONResponse(content="Delete movie genres", status_code=200)