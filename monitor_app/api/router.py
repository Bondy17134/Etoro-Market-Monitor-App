""" Handle the main router for the app (Centralized Routings) """
from fastapi import APIRouter
from monitor_app.api.v1.auth.routes import router as auth_router
from monitor_app.api.v1.user.routes import router as user_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(user_router, prefix="/users", tags=["Users"])
