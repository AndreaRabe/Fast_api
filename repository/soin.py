from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.Soin, db: Session):
    new_soin = models.Soin(rapport_soin=request.rapport_soin, date_debut=request.date_debut,date_fin=request.date_fin)
    db.add(new_soin)
    db.commit()
    db.refresh(new_soin)
    return new_soin

def showAll(db: Session):
    soins = db.query(models.Soin).all()
    return soins

def show(id: int, db: Session):
    soin = db.query(models.Soin).filter(models.Soin.id == id).first()
    if not soin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Care with the id {id} is not available")
    return soin

def destroy(id: int, db: Session):
    soin = db.query(models.Soin).filter(models.Soin.id == id)

    if not soin.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Care with id {id} not found")

    soin.delete()
    db.commit()
    return 'Delete successfull'

def update(id: int, request: schemas.Soin, db: Session):
    soin_data = dict(request)
    soin = db.query(models.Soin).filter(models.Soin.id == id)

    if not soin.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Care with id {id} not found")
    
    soin.update(soin_data)
    db.commit()
    return 'Updated successfull'