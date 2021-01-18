from typing import Optional
import datetime
from pydantic import BaseModel, EmailStr


# Shared properties
class CalendarEventBase(BaseModel):
    CalendarEvent: int
    title: str
    description: str
    startTime: datetime.datetime
    endTime: datetime.datetime




# Properties to receive via API on creation
class CalendarEventCreate(CalendarEventBase):
    pass

# Properties to receive via API on update
class CalendarEventUpdate(CalendarEventBase):
    pass


class CalendarEventInDBBase(CalendarEventBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class CalendarEvent(CalendarEventInDBBase):
    pass


# Additional properties stored in DB
class CalendarEventInDB(CalendarEventInDBBase):
    pass
