from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class ForumChannelBase(BaseModel):
    forumFolder: int
    channelName: str
    channelOrder: int
    requiredRank: int

# Properties to receive via API on creation
class ForumChannelCreate(ForumChannelBase):
    pass

# Properties to receive via API on update
class ForumChannelUpdate(ForumChannelBase):
    pass

class ForumChannelInDBBase(ForumChannelBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ForumChannel(ForumChannelInDBBase):
    pass


# Additional properties stored in DB
class ForumChannelInDB(ForumChannelInDBBase):
    pass