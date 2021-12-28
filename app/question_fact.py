
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from . import database

class change_data_type_factor(database.Base):
    __tablename__ = "question_factor_table"  # テーブル名を指定
    unique_student_id = Column(Integer, primary_key=True)
    student_name = Column(VARCHAR)
    question_b9_1 = Column(VARCHAR)
    question_c11_1 = Column(VARCHAR)
    question_c11_2 = Column(Integer)
    question_c11_3 = Column(Integer)
    question_c11_4 = Column(Integer)
    question_c11_5 = Column(Integer)
    question_c11_6 = Column(Integer)
    question_d12_1 = Column(Integer)
    question_d12_2 = Column(Integer)
    question_d12_3 = Column(Integer)
    question_d12_4 = Column(Integer)
    question_d12_5 = Column(Integer)
    question_d12_6 = Column(Integer)
    question_e13_1 = Column(Integer)
    question_e13_2 = Column(Integer)
    question_e13_3 = Column(Integer)
    question_e13_4 = Column(Integer)
    question_e13_5 = Column(Integer)
    question_e13_6 = Column(Integer)
    question_f14_1 = Column(Integer)
    question_f14_2 = Column(Integer)
    question_f14_3 = Column(Integer)
    question_f14_4 = Column(Integer)
    question_f14_5 = Column(Integer)
    question_f14_6 = Column(Integer)
    question_f14_7 = Column(Integer)
    question_g15_1 = Column(Integer)
    question_g15_2 = Column(Integer)
    question_g15_3 = Column(Integer)
    question_g15_4 = Column(Integer)




# create table question_factor_master(
# 	question_id 		integer  NOT NULL PRIMARY KEY,		-- 選択肢のマスター
# 	question_b9_1		varchar(255),						-- B9..一週間当たりの練習や勉強時間
# 	question_c11_1		varchar(255),						-- C11..レッスンのきっかけ.誰かからのプレッシャー
# 	question_c11_2		varchar(255),						-- C11..レッスンのきっかけ.友人からの刺激
# 	question_c11_3		varchar(255),						-- C11..レッスンのきっかけ.近親者からの勧め
# 	question_c11_4		varchar(255),						-- C11..レッスンのきっかけ.スキルの衰え
# 	question_c11_5		varchar(255),						-- C11..レッスンのきっかけ.キャリアに不安
# 	question_c11_6		varchar(255),						-- C11..レッスンのきっかけ.新しい趣味.特技
# 	question_d12_1		varchar(255),						-- D12..レッスンの目的.特技を通じた成長
# 	question_d12_2		varchar(255),						-- D12..レッスンの目的.人との繋がり
# 	question_d12_3		varchar(255),						-- D12..レッスンの目的.強みとして認識されたい
# 	question_d12_4		varchar(255),						-- D12..レッスンの目的.スキルレベルの維持
# 	question_d12_5		varchar(255),						-- D12..レッスンの目的.理想の自分になる
# 	question_d12_6		varchar(255),						-- D12..レッスンの目的.キャリアアップ
# 	question_e13_1		varchar(255),						-- E13..成果を見て貰いたい人.習い事.レッスンの先生
# 	question_e13_2		varchar(255),						-- E13..成果を見て貰いたい人.習い事.レッスンのコミュニティ
# 	question_e13_3		varchar(255),						-- E13..成果を見て貰いたい人.所属コミュニにティ学校.会社など
# 	question_e13_4		varchar(255),						-- E13..成果を見て貰いたい人.友人
# 	question_e13_5		varchar(255),						-- E13..成果を見て貰いたい人.恋人
# 	question_e13_6		varchar(255),						-- E13..成果を見て貰いたい人.家族
# 	question_f14_1		varchar(255),						-- F14..最も嬉しかった出来事.自分の成長を実感
# 	question_f14_2		varchar(255),						-- F14..最も嬉しかった出来事.仲間とともに成果を残した時
# 	question_f14_3		varchar(255),						-- F14..最も嬉しかった出来事.所属コミュニティに認められた時
# 	question_f14_4		varchar(255),						-- F14..最も嬉しかった出来事.先生に褒められた時
# 	question_f14_5		varchar(255),						-- F14..最も嬉しかった出来事.友達から褒められた時
# 	question_f14_6		varchar(255),						-- F14..最も嬉しかった出来事.近親者から褒められた時
# 	question_f14_7		varchar(255),						-- F14..最も嬉しかった出来事.資格を獲得できた時
# 	question_g15_1		varchar(255),						-- G15..独学でない理由.先生からの圧
# 	question_g15_2		varchar(255),						-- G15..独学でない理由.コミュニティに所属したい
# 	question_g15_3		varchar(255),						-- G15..独学でない理由.確実なスキルアップ
# 	question_g15_4		varchar(255)						-- G15..独学でない理由.独学への限界.
# );

