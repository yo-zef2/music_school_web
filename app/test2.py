
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker


# engine = create_engine("{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset={charset_type})".format(**{'dialect': 'postgresql',
# 'driver': 'psycopg2',
# 'user': 'ariikeisuke',
# 'password': 'candy1225',
# 'host': 'localhost',
# 'port': '5432',
# 'name': 'testdb',
# 'charset_type': 'utf8'
# })

db_url = ("{dialect}://{username}:{password}@{host}:{port}/{database}").format(
    **{'dialect': 'postgresql',
    'username': 'ariikeisuke',
    'password': 'candy1225',
    'host': 'localhost',
    'port': '5432',
    'database': 'testdb'})


engine = create_engine(db_url)
Base = declarative_base()

class User(Base):
    __tablename__ = "school_master"  # テーブル名を指定
    unique_school_id = Column(Integer, primary_key=True)
    school_name = Column(VARCHAR)
    nearest_station = Column(VARCHAR)
    address = Column(VARCHAR)
    operating_hour = Column(Integer)
    lesson_hour = Column(Integer)
    distance_station = Column(Integer)
    number_students = Column(Integer)
    lesson_time = Column(Integer)
    numbers_of_lesson = Column(Integer)
    price_minutes = Column(Integer)
    price_month = Column(Integer)

    def test(self):  # フルネームを返すメソッド
        return "{self.unique_school_id} {self.school_name}"

SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()

val_list = ['', '岩本町15', '']

for i in range(len(val_list)):
    if val_list[i] == '':
        val_list[i] = None

user_a = User(school_name=val_list[0], nearest_station=val_list[1], operating_hour = val_list[2])
session.add(user_a)
session.commit()

# users = session.query(User).all()
