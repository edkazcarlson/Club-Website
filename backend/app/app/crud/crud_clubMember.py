from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
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
        print(f"club member: {db_obj}")
        print(db_obj.id)
        db.add(db_obj)
        print(db_obj.id)
        db.commit()
        print(db_obj.id)
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: ClubMember, obj_in: Union[ClubMemberUpdate, Dict[str, Any]]
    ) -> ClubMember:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


clubMember = CRUDClubMember(ClubMember)
