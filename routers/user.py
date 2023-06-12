from fastapi import APIRouter, Depends, status
import schemas
from database import get_db
from sqlalchemy.orm import Session
from repository import users
from typing import List
from oauth2 import get_current_user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/new', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request : schemas.User, db : Session = Depends(get_db)):
    return users.create(request, db)

@router.get('/all', response_model=List[schemas.ShowUser], status_code=status.HTTP_200_OK)
def get_all( db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return users.get_all(db)

@router.get('/name/{name}', response_model=List[schemas.ShowUser], status_code=status.HTTP_200_OK)
def search_user(name : str, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return users.search_name(name, db) 

@router.get('/role/{role}', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def search_user_by_role(role : str, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return users.search_role(role, db)

@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_one(id : int, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return users.get_one(id, db)

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id : int , db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return users.delete(id, db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.User, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return users.updated(id, request, db)


# always put the body type of string before body type of int