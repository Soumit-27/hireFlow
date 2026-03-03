# schemas/auth.py

from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_validator

class UserRole(str, Enum):
    admin = "admin"
    hr = "hr"
    user = "user"

class RegisterSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=72)
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: UserRole
    company_name: Optional[str] = None

    @field_validator("company_name")
    @classmethod
    def validate_company(cls, v, info):
        role = info.data.get("role")
        if role == UserRole.hr and not v:
            raise ValueError("Company name is required for HR role")
        return v

class LoginSchema(BaseModel):
    email: EmailStr
    password: str