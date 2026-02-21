from fastapi import FastAPI
from app.registry import register_routes
from app.db.init_db import init_db

app = FastAPI(title="Fire Detection System")

@app.on_event("startup")
def on_startup():
    init_db()

register_routes(app)

@app.get("/")
def root():
    return {"message": "API is running"}