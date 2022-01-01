
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from . import Database

class FeatureValue(Database.Base):
    __tablename__ = "feature_value"  # テーブル名を指定
    unique_school_id = Column(Integer, primary_key=True)
    coaching_history = Column(Integer)
    t_childminder = Column(Boolean)
    t_kindergarden_teacher = Column(Boolean)
    t_vocal_music = Column(Boolean)
    t_beginner = Column(Boolean)
    t_contest = Column(Boolean)
    former_university = Column(VARCHAR)
    composition = Column(Boolean)
    study_abroad = Column(Boolean)
