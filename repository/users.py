from datetime import timedelta
from fastapi import HTTPException, status
import models, schemas
from hashing import Hash
from sqlalchemy.orm import Session

def create(request : schemas.User, db : Session):
    new_user = models.User(nom_utilisateur = request.nom_utilisateur, mot_de_passe = Hash.bcrypt(request.mot_de_passe), role = request.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_one(id : int, db : Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id : {id} not found')
    return user

def get_all(db : Session):
    user = db.query(models.User).all()
    return user

def delete(user_id : int, db : Session):
    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id : {user_id} not found')
    user.delete()
    db.commit()
    return 'Deleted successfully'

def updated(id : int, request : schemas.User, db : Session):
    request.mot_de_passe = Hash.bcrypt(request.mot_de_passe)
    user_data = dict(request)
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id : {id} not found')
    user.update(user_data)
    db.commit()
    return 'Updated successfully'

# future issu combine the fonction search

def search_name(name : str, db : Session):
    user = db.query(models.User).filter(models.User.nom_utilisateur.ilike(f"%{name}%")).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with this name : {name} not found')
    return user

def search_role(role : str, db : Session):
    user = db.query(models.User).filter(models.User.role == role).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Users with this role : {role} not found')
    return user
