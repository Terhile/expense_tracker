
from datetime import date

from pydantic import BaseModel


# Shared properties
class IncomeBase(BaseModel):
    amount: float
    description: str
    currency: str
    payer: str
    income_date: date
    is_deleted: bool
    earner_id: int


class IncomeCreate(IncomeBase):
    created_dt: date = date.today()


class IncomeUpdate(IncomeBase):
    last_updated: date = date.today()


# Properties shared by models stored in DB
class IncomeSchema(IncomeBase):
    id: int
    last_updated: date

    class Config:
        orm_mode = True
