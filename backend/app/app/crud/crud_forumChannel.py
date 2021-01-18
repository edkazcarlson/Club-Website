from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.forum import ForumChannel
from app.schemas.forumChannel import ForumChannelCreate, ForumChannelUpdate


class CRUDForumChannel(CRUDBase[ForumChannel, ForumChannelCreate, ForumChannelUpdate]):
    pass


forumChannel = CRUDForumChannel(ForumChannel)
