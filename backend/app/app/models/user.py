from typing import TYPE_CHECKING
from sqlalchemy import Table, Boolean, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from typing import TYPE_CHECKING
from sqlalchemy.ext import declarative

if TYPE_CHECKING:
    pass
declBase = declarative.declarative_base()

class UserToClub(Base):
    __tablename__ = 'UserToClub'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    club_id = Column(Integer, ForeignKey('club.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    pfp_Path = Column(String, default = "Default.bmp")
    clubs = relationship(
        "club",
        secondary='UserToClub',
        back_populates="user")

class Club(Base):
    __tablename__ = 'club'
    id = Column(Integer, primary_key=True, index=True)
    clubName = Column(String)
    clubIcon = Column(String)
    clubDescription = Column(String)
    clubLat = Column(Float)
    clubLong = Column(Float)
    members = relationship(
        "user",
        secondary='UserToClub',
        back_populates="club")