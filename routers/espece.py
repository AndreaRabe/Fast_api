from typing import List
from fastapi import APIRouter, Depends, status
import schemas
from sqlalchemy.orm import Session
from repository import espece
from database import get_db
from oauth2 import get_current_user

router = APIRouter(
    prefix="/espece",
    tags=['Especes']
)

@router.post('/new', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Espece, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return espece.create(request,db)

@router.get('/', response_model=List[schemas.ShowEspece])
def get_all(db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return espece.showAll(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowEspece)
def get_one(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return espece.show(id, db)

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return espece.destroy(id,db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Espece, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return espece.update(id, request, db)
