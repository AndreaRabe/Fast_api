from typing import List
from fastapi import APIRouter, Depends, status
import schemas
from sqlalchemy.orm import Session
from repository import suivi
from database import get_db
from oauth2 import get_current_user

router = APIRouter(
    prefix="/suivi",
    tags=['Suivis']
)

@router.post('/new', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Suivi, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return suivi.create(request,db)

@router.get('/all', response_model=List[schemas.ShowSuivi], status_code=status.HTTP_200_OK)
def get_all(db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return suivi.showAll(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowSuivi)
def get_one(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return suivi.show(id, db)

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return suivi.destroy(id,db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Suivi, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return suivi.update(id, request, db)
