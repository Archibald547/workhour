from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class IdMixin(object):
    id = Column(Integer, primary_key=True, index=True)

class TimestampMixin(object):
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class User(IdMixin, Base, TimestampMixin):

    __tablename__ = "user"

    username = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    # is_active = Column(Boolean, default=True)

    workhours = relationship("Workhour", back_populates="user")

class Task(IdMixin, Base, TimestampMixin):

    __tablename__ = "task"

    name = Column(String(255), index=True)
    fullname = Column(String(255))
    organization = Column(String(255))
    workhours = relationship("Workhour", back_populates="task")

class Workhour(IdMixin, Base, TimestampMixin):

    __tablename__ = "workhour"

    user_id = Column(Integer, ForeignKey("user.id"))
    task_id = Column(Integer, ForeignKey("task.id"))
    description = Column(String(255), index=True)

    user = relationship("User", back_populates="workhours")
    task = relationship("Task", back_populates="workhours")
