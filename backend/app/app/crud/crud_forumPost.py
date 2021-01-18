from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.forum import ForumPost
from app.schemas.forumPost import ForumPostCreate, ForumPostUpdate


class CRUDForumPost(CRUDBase[ForumPost, ForumPostCreate, ForumPostUpdate]):
    pass


forumPost = CRUDForumPost(ForumPost)
