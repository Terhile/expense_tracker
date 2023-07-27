
from sqlalchemy import Integer, Numeric, String, Boolean, Column, Date, ForeignKey
from ..crud.crud_base import Base
from sqlalchemy.orm import relationship


class IncomeModel(Base):
    __tablename__ = "Income"

    id = Column(Integer, primary_key=True, Index=True)
    amount = Column(Numeric, nullable=False)
    description = Column(String(1000), index=True, nullable=False)
    currency = Column(String(10), nullable=False)
    payer = Column(String(50), nullable=False, index=True)
    income_date = Column(Date, nullable=False)
    created_dt = Column(Date, nullable=False)
    last_updated = Column(Date, nullable=False)
    is_deleted = Column(Boolean)
    # earner_id = Column(Integer, ForeignKey("users.id"))

    # earnedby = relationship("users", back_populates="earnings")
