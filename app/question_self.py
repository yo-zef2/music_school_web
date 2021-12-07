
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from . import database

class change_data_type_self(database.Base):
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


# <!-- 
#     create table question_self_table(
#         unique_number_s     integer  NOT NULL PRIMARY KEY,  -- 生徒の連番
#         student_name        varchar(255),                   -- 生徒名
#         reason_a_1          integer,                        -- 習い事/レッスンを通っている理由 1, 通うことで、何か報酬(お金、昇級など)が 貰えるから
#         reason_b_2          integer,                        -- 習い事/レッスンを通っている理由 2, 通わないと、周りから怒られるから
#         reason_c_3          integer,                        -- 習い事/レッスンを通っている理由 3, 規則のようなものだから
#         reason_d_4          integer,                        -- 習い事/レッスンを通っている理由 4, 友人に良い印象を与えたいから
#         reason_e_5          integer,                        -- 習い事/レッスンを通っている理由 5, 辞めることに罪悪感があるから
#         reason_f_6          integer,                        -- 習い事/レッスンを通っている理由 6, 通わないと何となく不安だから
#         reason_g_7          integer,                        -- 習い事/レッスンを通っている理由 7 , 習い事/レッスンに通うことは良いことだ と思うから
#         reason_h_8          integer,                        -- 習い事/レッスンを通っている理由 8, 習い事/レッスンに通うことは大切なこと だと思うから
#         reason_i_9          integer,                        -- 習い事/レッスンを通っている理由 9, 習い事/レッスンの経験が社会では必要だ と思うから
#         reason_j_10         integer,                        -- 習い事/レッスンを通っている理由 10, 希望している進路(学校,会社,職種など)を 実現したいから
#         reason_k_11         integer,                        -- 習い事/レッスンを通っている理由 11, 将来の成功につながるから
#         reason_l_12         integer,                        -- 習い事/レッスンを通っている理由 12, 自分の夢を叶えたいから
#         reason_m_13         integer,                        -- 習い事/レッスンを通っている理由 13, 新しいスキルや技術の発見が面白いか ら
#         reason_n_14         integer,                        -- 習い事/レッスンを通っている理由 14, 自分の能力を磨き上げる過程で満足を感じるから
#         reason_o_15         integer                         -- 習い事/レッスンを通っている理由 15, この活動に本当に没頭しているとわくわくするから
#     ); -->
    