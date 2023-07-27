from fastapi import APIRouter, status
from database.crud import user_crud
from schemas import user_base
from database.crud import crud_base
from sqlalchemy.orm import Session
from fastapi import Depends
router = APIRouter()


def get_db():
    db = crud_base.make_session()
    try:
        yield db
    finally:
        db.close()


@router.post("/api/vi/users/", response_model=user_base.User, status_code=status.HTTP_201_CREATED)
async def add_new_user(new_user: user_base.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(new_user, db)


@router.get("/api/vi/users/{user_id}", response_model=user_base.User, status_code=status.HTTP_200_OK)
async def user_details_by_id(user_id: int, db: Session = Depends(get_db)):
    return user_crud.get_user_by_id(user_id, db)


@router.get("/api/vi/users/{email}", response_model=user_base.User, status_code=status.HTTP_200_OK)
async def user_details_by_email(email: int, db: Session = Depends(get_db)):
    return user_crud.get_user_by_email(email, db)
