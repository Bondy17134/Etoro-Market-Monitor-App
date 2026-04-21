""" Handle data validation of the app """

from pydantic import BaseModel

# User data models
class UserBase(BaseModel):
    # User must have username
    # username must be string
    username: str

# UserCreate inherits from UserBase and adds password field
# So, UserCreate has both username and password fields
class UserCreate(UserBase):
    password: str

class User(UserBase): 
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True