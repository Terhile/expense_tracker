
from ..models import user
from sqlalchemy.orm import Session

from core import security

from schemas import user_base


def get_user_by_id(id: int, db: Session):
    return db.query(user.UserModel).filter(user.UserModel.id == id).first()


def get_user_by_email(email: str, db: Session):
    return db.query(user.UserModel).filter(user.UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user.UserModel).offset(skip).limit(limit).all()


def create_user(user_to_add: user_base.UserCreate, db: Session):
    hashed_password = security.get_password_hash(user_to_add.password)
    db_user = user.UserModel(
        name=user_to_add.name, email=user_to_add.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
