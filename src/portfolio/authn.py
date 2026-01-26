from typing import NewType
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field

UserID = NewType("UserID", UUID)
Username = NewType("Username", str)
Email = EmailStr
Password = NewType("Password", str)

class BaseUser(BaseModel):
    """A user of the portfolio system."""

    id: UUID = Field(default_factory=uuid4)
    username: Username = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(...)
    password: Password = Field(..., min_length=8)

class UserSignup(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    username: str = Field(..., min_length=3, max_length=50)
    def is_valid(self) -> bool:
        return not (not self.email or not self.password or not self.username)
        return True
