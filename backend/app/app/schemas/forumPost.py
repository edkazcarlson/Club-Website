from typing import Optional
import datetime
from pydantic import BaseModel, EmailStr


# Shared properties
class ForumPostBase(BaseModel):
    channel: int
    writer: int
    timeStamp: datetime.datetime
    beenEdited: bool

# Properties to receive via API on creation
class ForumPostCreate(ForumPostBase):
    pass

# Properties to receive via API on update
class ForumPostUpdate(ForumPostBase):
    pass

class ForumPostInDBBase(ForumPostBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ForumPost(ForumPostInDBBase):
    pass


# Additional properties stored in DB
class ForumPostInDB(ForumPostInDBBase):
    pass