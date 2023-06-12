from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models, schemas


def create(request : schemas.Animals, db : Session):
    new_animals = models.Animal(genre = request.genre, age = request.age, poids = request.poids, sante = request.sante, progeniture = request.progeniture)
    db.add(new_animals)
    db.commit()
    db.refresh(new_animals)
    return new_animals

def get_all(db : Session):
    animals = db.query(models.Animal).all()
    return animals

def get_one(id : int, db : Session):
    animals = db.query(models.Animal).filter(models.Animal.id == id).first()
    if not animals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Animal with id : {id} not found')
    return animals

def search_genre(genre : bool, db : Session):
    animals = db.query(models.Animal).filter(models.Animal.genre == genre).all()
    if not animals:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Animals not found')
    return animals

def update(id : int, request : schemas.Animals, db : Session):
    animals_data = dict(request)
    animals = db.query(models.Animal).filter(models.Animal.id == id)
    if not animals.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Animal with id : {id} not found')
    animals.update(animals_data)
    db.commit()
    return 'Updated successfull'

def delete(id : int, db : Session):
    animals = db.query(models.Animal).filter(models.Animal.id == id)
    if not animals.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Animal with id : {id} not found')
    animals.delete()
    db.commit()
    return 'Deleted successfull'

