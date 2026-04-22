"""
Defines request and response schemas
"""
from pydantic import BaseModel, Field, ConfigDict, field_validator

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=72)

    @field_validator("password")
    @classmethod
    def validate_password_bytes(cls, value: str) -> str:
        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password must be 72 bytes or fewer")
        return value

class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)