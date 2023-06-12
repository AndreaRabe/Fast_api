from pydantic import BaseModel
from typing import List
from datetime import date

# schemas for all models
class User(BaseModel):
    nom_utilisateur : str
    mot_de_passe : str
    role : str

class Animals(BaseModel):
    genre : bool
    age : int
    poids : int
    sante : str
    progeniture : int | None = None

class Espece(BaseModel):
    nom_espece:str
    nombre:int

class Suivi(BaseModel):
    rapport_suivi:str
    date_suivi:date
    # user_id:int

class Soin(BaseModel):
    rapport_soin:str
    date_debut:date
    date_fin:date
    # user_id:int
    # suivi_id:int

class Produit(BaseModel):
    nom_produit:str
    quantite:int
    # espece_id:int

class Vente(BaseModel):
    prix:int
    date_expiration:date
    # produit_id:int
    # user_id:int

# schemas show models, modify for all routers

class ShowVente(Vente):
    produit : List[Vente] = []
    user : List[User] = []
    class Config():
        orm_mode = True

class ShowProduit(BaseModel):
    nom_produit:str
    quantite:int
    especes : List[Espece] | None = None
    ventes : List[Vente] | None = None
    class Config():
        orm_mode = True

class ShowSoin(BaseModel):
    rapport_soin : str
    date_debut : date
    date_fin : date
    user : List[User] | None = None
    suivi : List[Suivi] | None = None
    class Config():
        orm_mode = True

class ShowEspece(Espece):
    animaux : List[Animals] = []
    class Config():
        orm_mode = True


class ShowSuivi(Suivi):
    user : List[User] | None = None 
    soin : List[Soin] | None = None 
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    nom_utilisateur : str
    role : str
    animals : List[Animals] = []
    class Config():
        orm_mode = True

class ShowAnimal(BaseModel):
    genre : bool
    age : int
    poids : int
    sante : str
    progeniture : int | None = None
    user_animals : List[ShowUser] | None = None
    espece : List[Espece] | None = None
    class Config():
        orm_mode = True

# token and authentification

class Token(BaseModel):
    acces_token : str
    token_type : str

class TokenData(BaseModel):
    email : str | None = None


