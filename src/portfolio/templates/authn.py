from typing import NewType
import uuid
from pydantic import BaseModel

UserID = NewType("UserID", int)
Username = NewType("Username", str)
Email = NewType("Email", str)
Password = NewType("Password", str)

class User(BaseModel):
    """ A user of the portfolio system. """
    id: UserID
    username: Username
    email: Email
    password: Password

    @classmethod
    def create(cls, username: Username, email: Email, password: Password) -> "User":
        user_id = UserID(uuid.uuid4().int)
        return cls(id=user_id, username=username, email=email, password=password)

    @property
    def uuid_obj(self) -> uuid.UUID:
        return uuid.UUID(int=int(self.id))