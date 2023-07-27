from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys
import click
import urllib


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://u598251568_imoter:Imoter_2020@81.16.28.154:3306/u598251568_jellies"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
make_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = make_session()
    try:
        yield db
    finally:
        db.close()
