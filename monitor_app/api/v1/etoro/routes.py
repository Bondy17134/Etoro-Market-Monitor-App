""" Handle routing for Etoro related endpoints """
from fastapi import APIRouter
import requests
from monitor_app.core.config import get_setting
from monitor_app.core.http import headers

setting = get_setting()
router = APIRouter()

headers = headers

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