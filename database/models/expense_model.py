
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, Numeric, String
from database.crud.crud_base import Base


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100), index=True)
    amount = Column(Numeric, nullable=False)
    description = Column(String(1000), index=True, nullable=False)
    currency = Column(String(10), nullable=False)
    company = Column(String(100), nullable=False)
    expense_date = Column(DateTime, nullable=False, default=datetime.now())
    created_ts = Column(DateTime, nullable=False, default=datetime.now())
    updated_ts = Column(DateTime, nullable=False, default=datetime.now())
    is_deleted = Column(Boolean, default=False)
