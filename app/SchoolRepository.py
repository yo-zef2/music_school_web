from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from . import database
from . import school


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
        database.session.add(school_info)
        database.session.commit()

    def find_by_id(self,school_id):
        return database.session.query(
            school.school_master).filter(
                school.school_master.unique_school_id == school_id)
        
    def find_by_area(self, address):
        return database.session.query(
            school.school_master).filter(
                school.school_master.address.like("address%"))

