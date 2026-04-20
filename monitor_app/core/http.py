from monitor_app.core.config import get_setting 

headers = {
    "x-request-id": get_setting().request_id,
    "x-api-key": get_setting().api_key, 
    "x-user-key": get_setting().user_key
}