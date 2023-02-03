from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.reviewer import Reviewer
from config.database import Session
from service.reviewer import ReviewerService

reviewer_router = APIRouter()

@reviewer_router.get('/reviewer',tags=['reviewer'], response_model=Reviewer, status_code= 200)
def get_reviewer() ->Reviewer:   
    db = Session()
    result = ReviewerService(db).get_reviewer()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@reviewer_router.post('/reviewer', tags=['reviewer'], status_code=201 , response_model=dict)
def create_reviewer(reviewer:Reviewer) ->dict:
    db= Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse(content={'message':'reviewer save in data base'})

@reviewer_router.put('/reviewer{id}',tags=['reviewer'])
def update_reviewer(id:int,reviewer:Reviewer):
    db =  Session
    result = ReviewerService(db).get_reviewer(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    ReviewerService(db).update_reviewer(id,reviewer)
    return JSONResponse(content={"message":"Se ha modificado el reviewer con id: {id}"})

@reviewer_router.delete('/reviewer/{id}',tags=['reviewer'])
def delete_reviewer(id:int):
        db = Session()
        result = ReviewerService(db).delete_reviewer(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        return JSONResponse(content="Delete reviewer", status_code=200)
