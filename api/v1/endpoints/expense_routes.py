from ast import List
from fastapi import APIRouter, HTTPException, Response, status, Depends
from database.crud import crud_base, expense_crud
from sqlalchemy.orm import Session
from schemas.expense_schema import ExpenseCreate, ExpenseItem, ExpenseUpdate, Expenses
router = APIRouter()


@router.get("/expenses", response_model=Expenses)
async def expenses(db: Session = Depends(crud_base.get_db)):
    expenses = expense_crud.get_all_expenses(db)
    response = [Expenses(**expense) for expense in expenses]

    print(response)

    return response


@router.get("/expenses/{id}", response_model=ExpenseItem)
async def expenses(expense_id: int, db: Session = Depends(crud_base.get_db)):
    if expense_id <= 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return expense_crud.get_income_by_id(db, expense_id)


# @router.delete("/expenses/{id}")
# async def delete_expense(expense_id: int):
#     del expenses_data[expense_id]


@router.post("/expenses", status_code=status.HTTP_201_CREATED, response_model=ExpenseItem)
async def expense_create(input_data: ExpenseCreate, db: Session = Depends(crud_base.get_db)):
    return expense_crud.create_expense(db, input_data)


# @ router.put("/expenses/{id}")
# async def expense_update(expense_id: int, input_data: ExpenseUpdate):
#     if expense_id <= 0 or expense_id > len(expenses_data):
#         raise HTTPException(status_code=404, detail="Item not found")
#     expenses_data[expense_id-1] = dict(input_data)
