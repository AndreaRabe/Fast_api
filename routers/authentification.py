from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from jwtToken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
import schemas, database, models
from sqlalchemy.orm import Session
from hashing import Hash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



router = APIRouter(
    tags=['Authentification']
)

@router.post('/login')
def login(request : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(database.get_db)):
    user  = db.query(models.User).filter(models.User.nom_utilisateur == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials!!!')
    
    if not Hash.verify(user.mot_de_passe, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect password')
    
    access_token = create_access_token(
        data={"sub": user.nom_utilisateur }
    )
    return {"access_token": access_token, "token_type": "bearer"}
