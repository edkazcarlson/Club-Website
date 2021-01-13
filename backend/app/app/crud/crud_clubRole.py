from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.club import ClubRole
from app.schemas.clubRole import ClubRoleCreate, ClubRoleUpdate



class CRUDClubRole(CRUDBase[ClubRole, ClubRoleCreate, ClubRoleUpdate]):
    
    def create(self, db: Session, *, obj_in: ClubRoleCreate) -> ClubRole:
        db_obj = ClubRole(
            title = obj_in.title,
            club = obj_in.clubID, 
            color = "FFFFFF",
            canDeleteForum = False,
            canMuteUser = False,
            canBanUser = False,
            canKickUser = False,
            canAddEvents = False,
            canAnnounce = False,
            canDeleteClub = False,
            canChangeImages = False,
            roleRank = 0
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: ClubRole, obj_in: Union[ClubRoleUpdate, Dict[str, Any]]
    ) -> ClubRole:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


clubRole = CRUDClubRole(ClubRole)
