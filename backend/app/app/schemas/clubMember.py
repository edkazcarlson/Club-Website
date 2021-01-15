from typing import Optional
import datetime
from pydantic import BaseModel


# Shared properties
class ClubMemberBase(BaseModel):
    user: int
    club: int
    role: Optional[int]
    joined: Optional[datetime.datetime]


# Properties to receive via API on creation
class ClubMemberCreate(ClubMemberBase):
    user: int
    club: int

# Properties to receive via API on update
class ClubMemberUpdate(ClubMemberBase):
    pass    


class ClubMemberInDBBase(ClubMemberBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ClubMember(ClubMemberInDBBase):
    pass


# Additional properties stored in DB
class ClubMemberInDB(ClubMemberInDBBase):
    pass
