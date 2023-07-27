from sqlalchemy import Numeric, update
from sqlalchemy.orm import Session
from database.models.expense_model import Expense
from datetime import datetime
from schemas.expense_schema import ExpenseUpdate, ExpenseCreate


def get_income_by_id(db: Session, id: int):
    return db.query(Expense).filter(Expense.id == id).first()


def income_by_company(db: Session, company: str, skip: int = 0, limit: int = 100):
    return db.query(Expense).filter(Expense.comapny == company).offset(skip).limit(limit).all()


def get_all_expenses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Expense).offset(skip).limit(limit).all()


# def get_income_by_payer(db: Session, payer: str, skip: int = 0, limit: int = 100):
#     return db.query(Expense).filter(Expense.payer == payer).offset(skip).limit(limit).all()


def get_income_by_date_range(db: Session, start_date: datetime, end_date: datetime, skip: int = 0, limit: int = 100):
    return db.query(Expense).filter(Expense.income_date.between(start_date, end_date)).offset(skip).limit(limit).all()


def get_income_by_range(db: Session, lower_bound: Numeric, upper_bound: Numeric, skip: int = 0, limit: int = 100):
    return db.query(Expense).filter(Expense.amount.between(lower_bound, upper_bound)).offset(skip).limit(limit).all()


def create_expense(db: Session, new_income: ExpenseCreate):
    income_to_insert = Expense(**new_income.dict())
    # income_in_db = db.query(Expense).filter(Expense.earner_id == new_income.earner_id,
    #                                         Expense.amount == new_income.amount, Expense.income_date == new_income.income_date).count()
    # if income_in_db > 0:
    #     return income_to_insert

    db.add(income_to_insert)
    db.commit()
    db.refresh(income_to_insert)

    return income_to_insert


def update_income_details(db: Session, id: int, income_to_update: ExpenseUpdate):
    query = update(Expense).where(Expense.id ==
                                  id).values(Expense(**income_to_update.dict()))
    db.execute(query)
    db.commit()
