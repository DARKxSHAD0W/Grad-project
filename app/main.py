from fastapi import FastAPI
from app.api.camera_api import router as camera_router
from app.api.employee_api import router as employee_router #
from app.api.building_api import router as building_router
app = FastAPI(title="Fire Detection System")

app.include_router(camera_router, prefix="/api")
app.include_router(employee_router, prefix="/api")
app.include_router(building_router, prefix="/api")

@app.get("/")
def home():
    return {"status": "Fire Detection System API is Online"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)