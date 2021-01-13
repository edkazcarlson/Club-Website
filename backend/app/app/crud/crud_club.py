from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.club import Club
from app.schemas.club import ClubCreate, ClubUpdate

from app.crud.crud_clubRole import clubRole
from app.schemas.clubRole import ClubRoleCreate


class CRUDClub(CRUDBase[Club, ClubCreate, ClubUpdate]):
    
    def create(self, db: Session, *, obj_in: ClubCreate) -> Club:
        db_obj = Club(
            clubName = obj_in.clubName
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        print(f"db_obj: {db_obj}")
        print(f"db_obj.id: {db_obj.id}")
        defaultRoleSchema = ClubRoleCreate(title = 'Deafult', clubID = db_obj.id)
        defaultRole = clubRole.create(db = db, obj_in = defaultRoleSchema)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Club, obj_in: Union[ClubUpdate, Dict[str, Any]]
    ) -> Club:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
    # def addUser(self, db: Session, *, )



club = CRUDClub(Club)
