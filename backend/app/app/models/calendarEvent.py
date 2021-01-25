from typing import TYPE_CHECKING
from sqlalchemy import Table, Boolean, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

class CalendarEvent(Base):
    __tablename__ = 'calendarEvent'
    id = Column(Integer, primary_key=True, index=True)
    announcer = Column(Integer, ForeignKey('clubMember.id'))
    club = Column(Integer, ForeignKey('club.id'))
    title = Column(String)
    description = Column(String)
    startTime = Column(Date)
    endTime = Column(Date)
    # location = 
    recurring = Column(str) #Can be either 'Daily', 'Weekly', 'Monthly', 'Yearly'
    isNegativeEvent = Column(Boolean) #to do a 1 time removal of a recurring event
    isAllDay = Column(Boolean)
    


