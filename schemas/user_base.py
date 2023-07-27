
from schemas import income_base
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    hashed_password: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    # earnings: list[income_base.IncomeSchema] = None

    class Config:
        orm_mode = True
