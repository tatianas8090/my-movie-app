from typing import Optional
from fastapi import APIRouter,Path, Query, Depends
from pydantic import BaseModel, Field
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from models.genres import Genres as Genres


from config.database import Session
from schemas.genres import Genres as Genres
from service.genres import GenreService



genres_router =  APIRouter()


@genres_router.get('/genres', tags=['genres'], response_model=Genres, status_code=200 )
def get_genres() -> Genres:
    db = Session()
    result = GenreService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@genres_router.get('/genre{id}', tags=['genres'])
def get_director(id:int):
    db = Session()
    result = GenreService(db).get_genre_by_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)  

@genres_router.post('/genres', tags=['genres'],status_code=201, response_model=dict )
def create_genres(genres: Genres) -> dict:
    db = Session()
    result = GenreService(db).create_genre(genres)
    return JSONResponse(content=jsonable_encoder(result), status_code=201)

@genres_router.put('/genres/{id}',tags=['genres'])
def update_genre(id:int,genre:Genres):
    db =  Session()
    result = GenreService(db).get_genre_by_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    GenreService(db).update_genre(id,genre)
    return JSONResponse(content={"message":"Se ha modificado el Genre"})

@genres_router.delete('/genres/delete_genres/',tags=['genres'])
def delete_director(id:int):
    db = Session()
    result = GenreService(db).delete_genre(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content="Delete Genre", status_code=200)