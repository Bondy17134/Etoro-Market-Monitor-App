from fastapi import FastAPI
from monitor_app.api.router import router

app = FastAPI()

app.include_router(router, prefix="/main", tags=["Basic Information"])