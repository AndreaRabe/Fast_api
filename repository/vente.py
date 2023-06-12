from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.Vente, db: Session):
    new_vente = models.Vente(id=1,prix=request.prix, date_expiration=request.date_expiration)
    db.add(new_vente)
    db.commit()
    db.refresh(new_vente)
    return new_vente

def showAll(db: Session):
    ventes = db.query(models.Vente).all()
    return ventes

def show(id: int, db: Session):
    vente = db.query(models.Vente).filter(models.Vente.id == id).first()
    if not vente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sale with the id {id} is not available")
    return vente

def destroy(id: int, db: Session):
    vente = db.query(models.Vente).filter(models.Vente.id == id)

    if not vente.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sale with id {id} not found")

    vente.delete(synchronize_session=False)
    db.commit()
    return 'Deleted successful'


def update(id: int, request: schemas.Vente, db: Session):
    vente_data = dict(request)
    vente = db.query(models.Vente).filter(models.Vente.id == id)

    if not vente.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sale with id {id} not found")
    
    vente.update(vente_data)
    db.commit()
    return 'Updated successfull'
