from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.Suivi, db: Session):
    new_suivi = models.Suivi(rapport_suivi=request.rapport_suivi, date_suivi=request.date_suivi)
    db.add(new_suivi)
    db.commit()
    db.refresh(new_suivi)
    return new_suivi

def showAll(db: Session):
    suivis = db.query(models.Suivi).all()
    return suivis

def show(id: int, db: Session):
    suivi = db.query(models.Suivi).filter(models.Suivi.id == id).first()
    if not suivi:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Data with the id {id} is not available")
    return suivi

def update(id: int, request: schemas.Suivi, db: Session):
    suivi_data = dict(request)
    suivi = db.query(models.Suivi).filter(models.Suivi.id == id)

    if not suivi.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Data with id {id} not found")

    suivi.update(suivi_data)
    db.commit()
    return 'Updated successfull'

def destroy(id: int, db: Session):
    suivi = db.query(models.Suivi).filter(models.Suivi.id == id)

    if not suivi.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Data with id {id} not found")

    suivi.delete(synchronize_session=False)
    db.commit()
    return 'Deleted successfull'