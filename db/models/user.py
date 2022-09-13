import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

from db.db_setup import Base


class Role(enum.IntEnum):
    teacher = 1
    student = 2


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)

    profile = relationship('Profile', back_populates='owner', uselist=False)


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    new = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    owner = relationship('User', back_populates='profile')
