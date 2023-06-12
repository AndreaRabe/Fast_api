from fastapi import FastAPI
import models
from database import engine
from routers import user, authentification, vente, soin, produit, animals, suivi, espece

app =  FastAPI()

models.Base.metadata.create_all(bind = engine)


app.include_router(user.router)
app.include_router(authentification.router)
app.include_router(espece.router)
app.include_router(vente.router)
app.include_router(soin.router)
app.include_router(produit.router)
app.include_router(animals.router)
app.include_router(suivi.router)
