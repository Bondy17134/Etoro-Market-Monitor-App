"""
Defines request and response schemas
"""
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=72)

class UserResponse(UserBase):
    id: int

    class Config: 
        orm_mode = True