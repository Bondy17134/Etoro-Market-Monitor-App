""" 
Handles auth database models. (Later)
"""
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

    
"""
Token flow explanation:
1. User sends login request with username and password.
2. If credentials are valid, server generates an access token (e.g., JWT) 
    that contains user information (like username) and returns it to the client.
3. Client includes this token in the Authorization header of subsequent requests
    to access protected endpoints.
"""