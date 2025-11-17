from typing import NewType
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr

UserID = NewType("UserID", int)
Username = NewType("Username", str)
Email = EmailStr
Password = NewType("Password", str)

class BaseUser(BaseModel):
    """ A user of the portfolio system. """
    id: UUID = Field(default_factory=UUID)
    username: Username = Field(..., min_length=3, max_length=50)
    email: Email = Field(...)
    password: Password = Field(..., min_length=8)