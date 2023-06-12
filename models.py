from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import date
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    nom_utilisateur = Column(String(50))
    mot_de_passe = Column(String(200))
    role = Column(String(10))

    animals = relationship("Animal", back_populates="user_animals")
    suivis = relationship("Suivi", back_populates="user")
    
    ventes = relationship("Vente", back_populates="user")
    soins = relationship("Soin", back_populates="user")

class Animal(Base):
    __tablename__ = "Animals"
    id = Column(Integer, primary_key=True, index=True)
    genre = Column(Boolean)
    age = Column(Integer)
    poids = Column(Float)
    sante = Column(String(10))
    progeniture = Column(Integer)

    user_id = Column(Integer, ForeignKey("Users.id"))
    user_animals = relationship("User", back_populates="animals")

    espece_id = Column(Integer, ForeignKey('Especes.id'))
    espece = relationship("Espece", back_populates="animaux")

class Suivi(Base):
    __tablename__ = "Suivis"
    id = Column(Integer, primary_key=True, index=True)
    rapport_suivi = Column(String(150))
    date_suivi = Column(Date, default=date.today)

    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("User", back_populates="suivis")
    soin = relationship("Soin", back_populates="suivi")

class Soin(Base):
    __tablename__ = "Soins"
    id = Column(Integer, primary_key=True, index=True)
    rapport_soin = Column(String(150))
    date_debut = Column(Date)
    date_fin = Column(Date)

    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("User", back_populates="soins")

    suivi_id = Column(Integer, ForeignKey("Suivis.id"))
    suivi = relationship("Suivi", back_populates="soin")

class Espece(Base):
    __tablename__  = "Especes"
    id = Column(Integer, primary_key=True, index=True)
    nom_espece = Column(String(10))
    nombre = Column(Integer)

    animaux = relationship("Animal", back_populates="espece")

    produits = relationship("Produit", back_populates="espece")

class Produit(Base):
    __tablename__ = "Produits"
    id = Column(Integer, primary_key=True, index=True)
    nom_produit = Column(String(15))
    quantite = Column(Integer)

    espece_id = Column(Integer, ForeignKey("Especes.id"))
    espece = relationship("Espece", back_populates="produits")
    
    ventes = relationship("Vente", back_populates="produit")

class Vente(Base):
    __tablename__ = "Ventes"
    id = Column(Integer, primary_key=True, index=True)
    prix = Column(Integer)
    date_expiration = Column(Date)

    produit_id = Column(Integer, ForeignKey("Produits.id"))
    produit = relationship("Produit", back_populates="ventes")

    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("User", back_populates="ventes")
