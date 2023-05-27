from fastapi import FastAPI
from db import Base, engine
from routers import clients_router, dressmaker_router, dress_router


app = FastAPI()


Base.metadata.create_all(engine)


app.include_router(clients_router, tags=['Clients'])
app.include_router(dressmaker_router, tags=['Dressmaker'])
app.include_router(dress_router, tags=['Dress'])