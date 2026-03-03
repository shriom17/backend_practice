from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="User's name")
    email: EmailStr = Field(..., description="User's email address")


class UserCreate(UserBase):
    """Schema for creating a new user"""
    pass


class UserUpdate(BaseModel):
    """Schema for updating a user - all fields optional"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None


class UserResponse(UserBase):
    """Schema for user response"""
    id: int

    class Config:
        from_attributes = True
