from config import Config
from sqlalchemy import (Column, ForeignKey, String, Integer, DateTime, func)
from sqlalchemy.orm import (backref, relationship)
from sqlalchemy_utils import PasswordType, force_auto_coercion
from database import Base
from .role import Role

force_auto_coercion()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(
        PasswordType(onload=lambda **kwargs: dict(schemes=Config.PASSWORD_SCHEMES, **kwargs)),
        unique=False,
        nullable=False,
    )
    role_id = Column(Integer, ForeignKey('roles.id', name="USER_ROLE"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    roles = relationship(Role,
                         foreign_keys='User.role_id',
                         backref=backref('users', uselist=True, cascade='delete,all'))