from beanie import Document
from pydantic import EmailStr, Field
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    hr = "hr"
    user = "user"

class User(Document):
    name: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.user
    company_name: str | None = None
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"