
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# from app.app import school_master_db

db_url = ("{dialect}://{username}:{password}@{host}:{port}/{database}").format(
    **{'dialect': 'postgresql',
    'username': 'ariikeisuke',
    'password': 'candy1225',
    'host': 'localhost',
    'port': '5432',
    'database': 'testdb'})

engine = create_engine(db_url)
Base = declarative_base()

class school_master(Base):
    __tablename__ = "school_master"  # テーブル名を指定
    unique_school_id = Column(Integer, primary_key=True)
    school_name = Column(VARCHAR)
    nearest_station = Column(VARCHAR)
    address = Column(VARCHAR)
    operating_hour = Column(Integer)
    lesson_hour = Column(Integer)
    distance_station = Column(Integer)
    number_students = Column(Integer)
    lesson_time = Column(Integer)
    numbers_of_lesson = Column(Integer)
    price_minutes = Column(Integer)
    price_month = Column(Integer)
