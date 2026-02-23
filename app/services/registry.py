from app.api.auth_api import router as auth_router
from app.api.building_api import router as building_router
from app.api.employee_api import router as employee_router
from app.api.camera_api import router as camera_router
from app.api.ml_model_api import router as ml_model_router
from app.api.deployment_api import router as deployment_router
from app.api.fire_event_api import router as fire_event_router
from app.api.camera_action_api import router as camera_action_router


def register_routes(app):
    """
    Registers all routers with the FastAPI app.
    Prefixes and Tags are defined inside each individual router file.
    """
    # 0. Security First
    app.include_router(auth_router)

    # 1-3. Infrastructure
    app.include_router(building_router)
    app.include_router(employee_router)
    app.include_router(camera_router)

    # 4-5. AI Operations
    app.include_router(ml_model_router)
    app.include_router(deployment_router)

    # 6-7. Logs & Audits
    app.include_router(fire_event_router)
    app.include_router(camera_action_router)