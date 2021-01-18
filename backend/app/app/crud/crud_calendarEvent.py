from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.calendarEvent import CalendarEvent
from app.schemas.user import CalendarEventCreate, CalendarEventUpdate


class CRUDCalendarEvent(CRUDBase[CalendarEvent, CalendarEventCreate, CalendarEventUpdate]):
    pass
calendarEvent = CRUDCalendarEvent(CalendarEvent)
