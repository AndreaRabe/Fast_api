from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas
from sqlalchemy.orm import Session
from repository import soin
from database import get_db
from oauth2 import get_current_user

router = APIRouter(
    prefix="/soin",
    tags=['Soins']
)

@router.post('/new', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowSoin)
def create(request: schemas.Soin, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return soin.create(request,db)

@router.get('/all', response_model=List[schemas.ShowSoin])
def get_all(db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return soin.showAll(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowSoin)
def get_one(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return soin.show(id, db)

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return soin.destroy(id,db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Soin, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return soin.update(id, request, db)
