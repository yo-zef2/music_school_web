

from re import A
from flask import Flask,render_template,request
import psycopg2
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    instruments = ["ピアノ","ギター","ベース","ドラム"]
    return render_template("index.html",name=name,instruments=instruments)

db_url = ("{dialect}://{username}:{password}@{host}:{port}/{database}").format(
    **{'dialect': 'postgresql',
    'username': 'ariikeisuke',
    'password': 'candy1225',
    'host': 'localhost',
    'port': '5432',
    'database': 'testdb'})

engine = create_engine(db_url)
Base = declarative_base()
# SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
# session = SessionClass()


class school_master2(Base):
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


    # それぞれ格納された変数をDBにinsertする
insert_table = school_master2(
    school_name = 1,
    nearest_station = 2,
    address = 3,
    operating_hour = 4,
    lesson_hour = 5,
    distance_station = 5,
    number_students = 5,
    lesson_time = 6,
    numbers_of_lesson = 5,
    price_minutes = 6,
    price_month = 7)
    
print(insert_table)