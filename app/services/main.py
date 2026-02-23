from fastapi import FastAPI
from app.db.init_db import init_db
from app.registry import register_routes

app = FastAPI(title="Fire Detection System")

@app.on_event("startup")
def startup_event():
    # This MUST run first to build the tables
    init_db()

# Routes are registered second
register_routes(app)