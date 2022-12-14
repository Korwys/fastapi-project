import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

from db.db_setup import Base
from db.models.mixins import Timestamp


class Role(enum.IntEnum):
    teacher = 1
    student = 2


class User(Timestamp, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    profile = relationship('Profile', back_populates='owner', uselist=False)
    student_courses = relationship("StudentCourse", back_populates="student")
    student_content_blocks = relationship("CompletedContentBlock", back_populates="student")


class Profile(Timestamp, Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(Enum(Role))
    bio = Column(Text, nullable=True)
    new = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    owner = relationship('User', back_populates='profile')
