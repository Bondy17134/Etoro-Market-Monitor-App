""" Handle routing for portfolio related endpoints """
from fastapi import APIRouter
import requests
from monitor_app.api import router
from monitor_app.core.config import get_setting

setting = get_setting()

headers = {
    "x-request-id": setting.request_id,
    "x-api-key": setting.api_key, 
    "x-user-key": setting.user_key
}

@router.get("/portfolio", name="Portfolio")
def get_portfolio():
    username = "KunanonToonsap"
    api_url = f"https://public-api.etoro.com/api/v1/user-info/people/{username}/portfolio/live"
    response = requests.get(
        api_url,
        headers=headers
    )
    return response.json()