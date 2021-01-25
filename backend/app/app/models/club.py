from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    pass

class Club(Base):
    __tablename__ = 'club'
    id = Column(Integer, primary_key=True, index=True)
    clubName = Column(String)
    clubIcon = Column(String)
    clubDescription = Column(String)
    clubLat = Column(Float)
    clubLong = Column(Float)
    clubColor = Column(String)

class ClubRole(Base):
    __tablename__ = 'clubRole'
    id = Column(Integer, primary_key = True, index = True)
    club = Column(Integer, ForeignKey('club.id'))
    title = Column(String)
    color = Column(String)
    canDeleteForum = Column(Boolean)
    canMuteUser = Column(Boolean)
    canBanUser = Column(Boolean)
    canKickUser = Column(Boolean)
    canAddEvents = Column(Boolean)
    canAnnounce = Column(Boolean)
    canDeleteClub = Column(Boolean)
    canChangeImages = Column(Boolean)
    canManageFunds = Column(Boolean)
    canDecideAds = Column(Boolean)
    roleRank = Column(Integer)

class ClubMember(Base):
    __tablename__ = 'clubMember'
    id = Column(Integer, primary_key = True, index = True)
    user = Column(Integer,  ForeignKey('user.id'))
    club = Column(Integer, ForeignKey('club.id'))
    role = Column(Integer, ForeignKey('clubRole.id'))
    joined = Column(Date)