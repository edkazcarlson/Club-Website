from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.db.base_class import Base

class AssocTable(Base):
    __tablename__ = 'AssocTable'
    id = Column(Integer, primary_key = True)
    left_id = Column(Integer, ForeignKey('left.id'))
    right_id = Column(Integer, ForeignKey('right.id'))

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship(
        "Child",
        secondary='AssocTable',
        back_populates="parents")

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship(
        "Parent",
        secondary='AssocTable',
        back_populates="children")