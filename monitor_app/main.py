from fastapi import FastAPI
from monitor_app.api.router import router
from monitor_app.api.v1.auth.routes import router as auth_router
from monitor_app.api.v1.users.routes import router as users_router

# Create the FastAPI app
app = FastAPI()

# Include routes from router.py
app.include_router(router, prefix="/api/v1", tags=["Basic Information"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI authentication and authorisation"}