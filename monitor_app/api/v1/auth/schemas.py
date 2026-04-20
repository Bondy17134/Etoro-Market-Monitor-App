"""
Defines request and response schemas
"""
from pydantic import BaseModel

# A passing ticket after successful login
# returned to client after successful login
class Token(BaseModel):
    # string value that represents the access token
    access_token: str
    # string value that represents the type of token (e.g., "bearer")
    token_type: str

# Data contained in the token, such as the username of the authenticated user
# get it when decoding the token to verify the user's identity
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