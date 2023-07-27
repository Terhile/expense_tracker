from sqlalchemy import Integer, String, Boolean, Column, Date
from ..crud.crud_base import Base
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(2000))
    is_active = Column(Boolean, default=True)

    # earnings = relationship("Income", back_populates="earnedby")
