from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class ForumFolderBase(BaseModel):
    club: int
    folderName: str
    folderOrder: int

# Properties to receive via API on creation
class ForumFolderCreate(ForumFolderBase):
    pass

# Properties to receive via API on update
class ForumFolderUpdate(ForumFolderBase):
    pass

class ForumFolderInDBBase(ForumFolderBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ForumFolder(ForumFolderInDBBase):
    pass


# Additional properties stored in DB
class ForumFolderInDB(ForumFolderInDBBase):
    pass