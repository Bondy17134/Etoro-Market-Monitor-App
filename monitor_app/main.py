from fastapi import FastAPI
import requests 

app = FastAPI()

@app.get("/")
def root():
    return {'message': 'Welcome to Etoro Market Monitor App'}

@app.get("/get_list")
def get_list():
    api_url = "https://public-api.etoro.com/api/v1/curated-lists"
    all_lists = requests.get(api_url).json()
    return all_lists