from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status


def create(request: schemas.Produit, db: Session):
    new_produit = models.Produit(nom_produit=request.nom_produit, quantite=request.quantite)
    db.add(new_produit)
    db.commit()
    db.refresh(new_produit)
    return new_produit

def showAll(db: Session):
    prod = db.query(models.Produit).all()
    return prod

def show(id: int, db: Session):
    prod = db.query(models.Produit).filter(models.Produit.id == id).first()
    if not prod:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with the id {id} is not available")
    return prod

def destroy(id: int, db: Session):
    prod = db.query(models.Produit).filter(models.Produit.id == id)

    if not prod.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")

    prod.delete()
    db.commit()
    return 'Deleted successfull'

def update(id: int, request: schemas.Produit, db: Session):
    product_data = dict(request)
    prod = db.query(models.Produit).filter(models.Produit.id == id)

    if not prod.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")

    prod.update(product_data)
    db.commit()
    return 'Updated successfull'
