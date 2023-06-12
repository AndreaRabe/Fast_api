from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.Espece, db: Session):
    new_espece = models.Espece(nom_espece=request.nom_espece, nombre=request.nombre)
    db.add(new_espece)
    db.commit()
    db.refresh(new_espece)
    return new_espece

def showAll(db: Session):
    esp = db.query(models.Espece).all()
    return esp

def show(id: int, db: Session):
    esp = db.query(models.Espece).filter(models.Espece.id == id).first()
    if not esp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Espece with the id {id} is not found")
    return esp

def update(id: int, request: schemas.Espece, db: Session):
    espece_data = dict(request)
    esp = db.query(models.Espece).filter(models.Espece.id == id)

    if not esp.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Espece with id {id} not found")
    
    esp.update(espece_data)
    db.commit()
    return 'Updated successfull'

def destroy(id: int, db: Session):
    esp = db.query(models.Espece).filter(models.Espece.id == id)

    if not esp.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Espece with id {id} not found")

    esp.delete(synchronize_session=False)
    db.commit()
    return 'Deleted successfull'