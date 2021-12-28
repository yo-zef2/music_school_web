from re import S
from flask import Flask,render_template,request
import psycopg2
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.expression import insert
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
# from . import school
# from . import database
# from . import feature_value
# from . import method
# from . import question_self
# from . import question_fact
# from . import student_master_info
from SchoolRepository import SchoolRepository



test = SchoolRepository()
test.find_by_id(100)