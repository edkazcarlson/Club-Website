from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from sqlalchemy import join
from app.core.security import get_password_hash, verify_password

from app.models.club import Club, ClubRole

from app.crud.base import CRUDBase
from app.crud.crud_clubMember import clubMember
from app.crud.crud_clubRole import clubRole
from app.crud.crud_forumFolder import forumFolder
from app.crud.crud_forumChannel import forumChannel


from app.schemas.clubRole import ClubRoleCreate
from app.schemas.clubMember import ClubMemberCreate
from app.schemas.club import ClubCreate, ClubUpdate
from app.schemas.forumFolder import ForumFolderCreate, ForumFolderUpdate
from app.schemas.forumChannel import ForumChannelCreate, ForumChannelUpdate

from sqlalchemy import desc

import datetime

class CRUDClub(CRUDBase[Club, ClubCreate, ClubUpdate]):
    
    def create(self, db: Session, *, obj_in: ClubCreate) -> Club:
        db_objSchema = Club(
            clubName = obj_in.clubName
        )
        db.add(db_objSchema)
        db.commit()
        db.refresh(db_objSchema)

        defaultRoleSchema = ClubRoleCreate(title = 'Deafult', clubID = db_objSchema.id)
        defaultRole = clubRole.create(db = db, obj_in = defaultRoleSchema)

        OwnerRoleSchema = ClubRoleCreate(title = 'Owner', clubID = db_objSchema.id)
        OwnerRole = clubRole.createOwner(db = db, obj_in = OwnerRoleSchema)

        defaultForumSchema = ForumFolderCreate(club = db_objSchema.id, folderName = 'General', folderOrder = 0)
        defaultForum = forumFolder.create(db = db, obj_in = defaultForumSchema)

        defaultChannelSchema = ForumChannelCreate( forumFolder = defaultForum.id, \
            channelName = 'General', channelOrder = 0, requiredRank =  0)
        defaultChannel = forumChannel.create(db = db, obj_in = defaultChannelSchema)
        return db_objSchema

    def update(
        self, db: Session, *, db_obj: Club, obj_in: Union[ClubUpdate, Dict[str, Any]]
    ) -> Club:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
    def addUser(self, db: Session, *, clubID: int, userId: int):
        newMember = ClubMemberCreate(user = userId, club = clubID, role = 0, joined = datetime.datetime.now())
        clubMember.create(db, obj_in = newMember)

    def getDefaultRole(self, db: Session, *, clubID: int):
        thisClubID = self.get(db, clubID).id
        j = db.query(ClubRole).filter(ClubRole.club == clubID).order_by(desc(ClubRole.roleRank)).limit(1)
        print('join here')
        for row in j:
            return row
        return 'Could not find a role'
        

club = CRUDClub(Club)
