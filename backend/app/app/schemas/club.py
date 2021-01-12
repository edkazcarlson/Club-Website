from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class ClubBase(BaseModel):
    clubName: str
    clubDescription: Optional[str]
    clubIcon: Optional[str]
    clubLat: Optional[float]
    clubLong: Optional[float]



# Properties to receive via API on creation
class ClubCreate(ClubBase):
    clubName: str


# Properties to receive via API on update
class ClubUpdate(ClubBase):
    clubDescription: Optional[str] = None
    clubIcon: Optional[str] = None
    clubLat: Optional[float] = None
    clubLong: Optional[float] = None


class ClubInDBBase(ClubBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Club(ClubInDBBase):
    pass


# Additional properties stored in DB
class ClubInDB(ClubInDBBase):
    pass
