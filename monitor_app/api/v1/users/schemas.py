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

# Data sent back to client after user creation
class UserResponse(UserBase):
    id: int 

    class Config:
        orm_mode = True
    
    # for modern pydantic v2
    #model_config = ConfigDict(from_attributes=True)
