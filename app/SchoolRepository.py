from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from . import Database
from .SchoolMaster import SchoolMaster


class SchoolRepository:

    def insert_data(self,school_info):
        Database.session.add(school_info)
        Database.session.commit()

    def find_by_id(self,school_id):
        return Database.session.query(
            SchoolMaster).filter(
                SchoolMaster.unique_school_id == school_id)
        
    def find_by_area(self, address):
        return Database.session.query(
            SchoolMaster).filter(
                SchoolMaster.address.like("address%"))

