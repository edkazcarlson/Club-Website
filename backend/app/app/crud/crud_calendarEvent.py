from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.calendarEvent import CalendarEvent
from app.schemas.calendarEvent import CalendarEventCreate, CalendarEventUpdate
from app.models.club import ClubMember

class CRUDCalendarEvent(CRUDBase[CalendarEvent, CalendarEventCreate, CalendarEventUpdate]):
    def create(self, db: Session, *, obj_in: CalendarEventCreate, announcer: int, club: int) -> CalendarEvent:
        db_obj = CalendarEvent(
            club = club,
            title = obj_in.title,
            description = obj_in.description,
            startTime = obj_in.startTime,
            endTime = obj_in.endTime,
            announcer = announcer,
            recurring = obj_in.recurring,
            isNegativeEvent = obj_in.isNegativeEvent,
            isAllDay = obj_in.isAllDay
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
calendarEvent = CRUDCalendarEvent(CalendarEvent)
