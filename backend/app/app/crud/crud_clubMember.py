from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.club import ClubMember
from app.schemas.clubMember import ClubMemberCreate, ClubMemberUpdate



class CRUDClubMember(CRUDBase[ClubMember, ClubMemberCreate, ClubMemberUpdate]):
    
    def create(self, db: Session, *, obj_in: ClubMemberCreate) -> ClubMember:
        db_obj = ClubMember(
            clubName = obj_in.clubName
        )
        db.add(db_obj)
        db.commit()
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


ClubMember = CRUDClubMember(ClubMember)
