from fastapi import FastAPI
from monitor_app.api.router import router

# Create the FastAPI app
app = FastAPI()

# Include routes from router.py
app.include_router(router, prefix="/api/v1", tags=["Basic Information"])