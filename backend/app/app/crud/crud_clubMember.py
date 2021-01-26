from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.club import ClubRole
from app.models.club import ClubMember
from app.schemas.clubMember import ClubMemberCreate, ClubMemberUpdate
from app import crud

import datetime

class CRUDClubMember(CRUDBase[ClubMember, ClubMemberCreate, ClubMemberUpdate]):
    
    def create(self, db: Session, *, obj_in: ClubMemberCreate) -> ClubMember:
        rank = crud.club.getDefaultRole(db = db, clubID = obj_in.club)
        if rank == 'Could not find a role':
            return rank
        db_obj = ClubMember(
            club = obj_in.club,
            user = obj_in.user,
            role = rank.id,
            joined = datetime.datetime.now()
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def getMemberFromUser(self, db: Session, *, userID: int, clubID: int):
        q = db.query(ClubMember).filter(ClubMember.club == clubID and ClubMember.user == userID).limit(1)
        for row in q:
            return row
        return None

    def update(
        self, db: Session, *, db_obj: ClubMember, obj_in: Union[ClubMemberUpdate, Dict[str, Any]]
    ) -> ClubMember:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    
    def canAnnounce(self, db: Session, *, memberID: int):
        q = db.query(ClubMember).filter(ClubMember.id == memberID).limit(1)
        for row in q:
            role = db.query(ClubRole).filter(ClubRole.roleRank == row.role)
            if role == None:
                return False
            if role.canAnnounce:
                return True
            else:
                return False
        return False

clubMember = CRUDClubMember(ClubMember)
