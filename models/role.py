from sqlalchemy import (Column, String, Integer, DateTime, func)
from sqlalchemy_utils import force_auto_coercion
from database import Base

force_auto_coercion()


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())