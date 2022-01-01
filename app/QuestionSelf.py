
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from . import Database

class QuestionSelf(Database.Base):
    __tablename__ = "question_self_table"  # テーブル名を指定
    unique_student_id = Column(Integer, primary_key=True)
    student_name = Column(VARCHAR)
    reason_a_1 = Column(Integer)
    reason_b_2 = Column(Integer)
    reason_c_3 = Column(Integer)
    reason_d_4 = Column(Integer)
    reason_e_5 = Column(Integer)
    reason_f_6 = Column(Integer)
    reason_g_7 = Column(Integer)
    reason_h_8 = Column(Integer)
    reason_i_9 = Column(Integer)
    reason_j_10 = Column(Integer)
    reason_k_11 = Column(Integer)
    reason_l_12 = Column(Integer)
    reason_m_13 = Column(Integer)
    reason_n_14 = Column(Integer)
    reason_o_15 = Column(Integer)
    