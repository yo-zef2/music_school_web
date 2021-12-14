
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from . import database

class change_data_type_student_master(database.Base):
    __tablename__ = "student_master"  # テーブル名を指定
    unique_student_id = Column(Integer, primary_key=True)
    student_name = Column(VARCHAR)
    school_name = Column(VARCHAR)
    student_age = Column(Integer)
    family_structure = Column(Integer)
    student_address = Column(VARCHAR)
    playing_history = Column(Integer)
    learning_history = Column(Integer)
    performance_level = Column(Integer)
    achivement_homework = Column(Integer)
    purpose_lesson = Column(Integer)
    participation_consert = Column(Integer)

#   unique_student_id	    integer NOT NULL PRIMARY KEY,		-- 連番
#   student_name     		varchar(255),                       -- 生徒名(仮名)
#   school_name      		varchar(255),						-- 教室名
#   student_age      		integer,							-- 生徒の年齢
#   family_structure 		integer,							-- 家族構成
#   student_address  	varchar(255),				     	   -- 生徒の住所
#   playing_history  		integer,						   -- 演奏歴
#   learning_history 		integer,						   -- レッスン歴
#   performance_level 	integer,						   -- 演奏レベル
#   achivement_homework   integer,						   -- 宿題の進捗度
#   purpose_lesson 		integer,						   -- レッスンの目的	
#   participation_consert integer							   -- 発表回の参加回数
    