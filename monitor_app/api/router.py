""" Handle the access routing of the App"""

from fastapi import APIRouter
import requests
from monitor_app.config.config import get_setting

router = APIRouter()

setting = get_setting()

# Temporary
headers = {
    "x-request-id": setting.request_id,
    "x-api-key": setting.api_key,
    "x-user-key": setting.user_key
}

@router.get("/curated_list", name = "Curated investment lists")
def get_curated_list():
    api_url = "https://public-api.etoro.com/api/v1/curated-lists"
    headers 
    response = requests.get(
        api_url,
        headers=headers
    )
    return response.json()

@router.get("/watchlist", name = "Watchlists")
def get_watchlist():
    api_url = "https://public-api.etoro.com/api/v1/watchlists?itemsPerPageForSingle=100&ensureBuiltinWatchlists=true"
    headers 
    response = requests.get(
        api_url,
        headers=headers
    )
    return response.json()

@router.get("/portfolio", name = "Portfolio")
def get_portfolio():
    username = "KunanonToonsap"
    api_url = f"https://public-api.etoro.com/api/v1/user-info/people/{username}/portfolio/live"
    headers 
    response = requests.get(
        api_url,
        headers=headers
    )
    return response.json()