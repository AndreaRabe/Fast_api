from typing import List
from fastapi import APIRouter, Depends, status
import schemas
from sqlalchemy.orm import Session
from repository import produit
from database import get_db
from oauth2 import get_current_user

router = APIRouter(
    prefix="/produit",
    tags=['Produits']
)

@router.post('/new', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowProduit)
def create(request: schemas.Produit, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return produit.create(request,db)

@router.get('/all', response_model=List[schemas.ShowProduit])
def get_all(db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return produit.showAll(db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowProduit)
def get_one(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return produit.show(id, db)

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return produit.destroy(id,db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Produit, db: Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return produit.update(id, request, db)
