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
    current_user: models.User = Depends(deps.get_current_active_superuser),
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
    # current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new club.
    """
    club = crud.club.create(db, obj_in=club_in)
    return club

