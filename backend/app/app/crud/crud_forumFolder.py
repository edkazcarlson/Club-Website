from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.forum import ForumFolder
from app.schemas.forumFolder import ForumFolderCreate, ForumFolderUpdate


class CRUDForumFolder(CRUDBase[ForumFolder, ForumFolderCreate, ForumFolderUpdate]):
    pass


forumFolder = CRUDForumFolder(ForumFolder)
