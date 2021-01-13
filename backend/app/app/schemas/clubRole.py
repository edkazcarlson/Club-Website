from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class ClubRoleBase(BaseModel):
    title : str
    color : str = 'FFFFFF'
    canDeleteForum: bool
    canMuteUser : bool
    canBanUser : bool
    canKickUser : bool
    canAddEvents : bool
    canAnnounce : bool
    canDeleteClub : bool
    canChangeImages : bool
    roleRank: int


# Properties to receive via API on creation
class ClubRoleCreate(ClubRoleBase):
    title: str
    clubID: int
    color : str = 'FFFFFF'
    canDeleteForum: bool = False
    canMuteUser : bool= False
    canBanUser : bool= False
    canKickUser : bool= False
    canAddEvents : bool= False
    canAnnounce : bool= False
    canDeleteClub : bool= False
    canChangeImages : bool= False
    roleRank: int = 0

# Properties to receive via API on update
class ClubRoleUpdate(ClubRoleBase):
    pass    


class ClubRoleInDBBase(ClubRoleBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ClubRole(ClubRoleInDBBase):
    pass


# Additional properties stored in DB
class ClubRolenDB(ClubRoleInDBBase):
    pass
