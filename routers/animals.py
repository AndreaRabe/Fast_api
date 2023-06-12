from fastapi import APIRouter, status, Depends
import schemas
from sqlalchemy.orm import Session
from database import get_db
from repository import animals
from typing import List
from oauth2 import get_current_user

router = APIRouter(
    prefix='/animals',
    tags=['Animals']
)

@router.post('/new', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowAnimal)
def create(request : schemas.Animals, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return animals.create(request, db)

@router.get('/all', response_model=List[schemas.ShowAnimal],status_code=status.HTTP_200_OK)
def get_all(db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return animals.get_all(db)

@router.get('/genre/{genre}', response_model=List[schemas.ShowAnimal], status_code=status.HTTP_200_OK)
def search_genre(genre : bool, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return animals.search_genre(genre, db)

@router.get('/{id}', response_model=schemas.ShowAnimal, status_code=status.HTTP_200_OK)
def get_one(id : int, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return animals.get_one(id, db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.Animals, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return animals.update(id, request, db)

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id : int, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return animals.delete(id, db)
