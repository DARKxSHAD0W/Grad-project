from fastapi import FastAPI
from app.api.building_api import router as building_router
from app.api.employee_api import router as employee_router
from app.api.camera_api import router as camera_router

# You will add camera_router, ml_model_router, etc., here later

def register_routes(app: FastAPI):
    """
    This function initializes all routers and attaches them to the FastAPI app.
    It follows the teacher's requirement for a centralized communication module.
    """
    # Register Buildings CRUD
    app.include_router(
        building_router,
        prefix="/api/buildings",
        tags=["Buildings"]
    )

    # Register Employees CRUD (including Bcrypt encryption)
    app.include_router(
        employee_router,
        prefix="/api/employees",
        tags=["Employees"]
    )

    app.include_router(
        camera_router,
        prefix="/api/cameras",
        tags=["Cameras"]
    )

    # Example for future tables:
    # app.include_router(camera_router, prefix="/api/cameras", tags=["Cameras"])