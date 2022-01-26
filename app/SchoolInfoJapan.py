
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from . import Database

class SchoolInforJapan(Database.Base):
    __tablename__ = "school_info_japan"  # テーブル名を指定
    school_id_web = Column(Integer, primary_key=True)
    address = Column(VARCHAR)
    count_school_num = Column(Integer)
    average_price = Column(Integer)
    max_price = Column(Integer)
    min_price = Column(Integer)
