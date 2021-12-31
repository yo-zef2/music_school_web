from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from . import Database
from .SchoolMaster import SchoolMaster


# db_url = ("{dialect}://{username}:{password}@{host}:{port}/{database}").format(
#     **{'dialect': 'postgresql',
#     'username': 'ariikeisuke',
#     'password': 'candy1225',
#     'host': 'localhost',
#     'port': '5432',
#     'database': 'testdb'})

# engine = create_engine(db_url)
# Base = declarative_base()
# SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
# session = SessionClass()


class SchoolRepository:

    def insert_data(self,school_info):
        Database.session.add(school_info)
        Database.session.commit()

    def find_by_id(self,school_id):
        return Database.session.query(
            SchoolMaster.school_master).filter(
                SchoolMaster.school_master.unique_school_id == school_id)
        
    def find_by_area(self, address):
        return Database.session.query(
            SchoolMaster.school_master).filter(
                SchoolMaster.school_master.address.like("address%"))

