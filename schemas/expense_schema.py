
from typing import List
from datetime import datetime
from pydantic import BaseModel


class ExpenseBase(BaseModel):
    expense_date: datetime = datetime.now()
    amount: float
    currency: str
    category: str
    description: str
    company: str


class ExpenseCreate(ExpenseBase):
    created_ts: datetime = datetime.now()


class ExpenseUpdate(ExpenseBase):
    updated_ts: datetime = datetime.now()


class ExpenseItem(ExpenseBase):
    id: int
    is_deleted: bool = False

    class Config:
        orm_mode = True


class Expenses(ExpenseItem):
    all_expenses: List[ExpenseItem] = []
