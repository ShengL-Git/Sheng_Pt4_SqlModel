from fastapi import FastAPI
from database import lifespan

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"message":"Welcome to FastAPI and SQLModel"}

@app.get("/customer")
def customer():
    return customer
