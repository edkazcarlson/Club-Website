from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email
import os 
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/", response_model=List[schemas.Club])
def read_clubs(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    currentUser: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve clubs.
    """
    clubs = crud.club.get_multi(db, skip=skip, limit=limit)
    return clubs


@router.post("/", response_model=schemas.Club)
def create_club(
    *,
    db: Session = Depends(deps.get_db),
    club_in: schemas.ClubCreate,
    currentUser: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new club.
    """
    club = crud.club.create(db, obj_in=club_in)
    return club

@router.post("/addEvent/{clubID}", response_model=str)
def create_event(
    *,
    db: Session = Depends(deps.get_db),
    clubID: int,
    calendarIn: schemas.CalendarEventCreate,
    currentUser: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new event for a club.
    """
    club = crud.club.get(db = db, id = clubID)
    if club != None:
        member = crud.clubMember.getMemberFromUser(db = db, userID = currentUser.id, clubID = club.id)
        if member != None:
            if crud.clubMember.canAnnounce(db = db, memberID = member.id):
                newEvent = crud.calendarEvent.create(db, obj_in = calendarIn, announcer =  member.id, club = club.id)
            else:
                return 'Insufficient permissions to announce'
            return newEvent.id
        else:
            return 'Not a member of the club'
    else:
        return 'No club with this id found'
