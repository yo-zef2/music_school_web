from flask import Flask,render_template,request
import psycopg2
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from . import school

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
SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()

@app.route("/add",methods=["post"])
def post():
    # Webページで記入された内容を変数に格納する
    school_name = request.form["school_name"]
    nearest_station = request.form["station"]   
    address = request.form["address"]
    operating_hour = request.form["operating_hour"]
    lesson_hour = request.form["lesson_hour"]
    distance_station = request.form["distance"]
    number_students = request.form["number_student"]
    lesson_time = request.form["lesson_time"]
    numbers_of_lesson = request.form["numbers_of_lesson"]
    price_minutes = request.form["price_minutes"]
    price_month = request.form["price_month"]

    # 空欄の場合の''について、NULL型に変換する処理を行う
    val_list = [
        school_name,
        nearest_station,
        address,
        operating_hour,
        lesson_hour,
        distance_station,
        number_students,
        lesson_time,
        numbers_of_lesson,
        price_minutes,
        price_month]

    for i in range(len(val_list)):
        if val_list[i] == '':
            val_list[i] = None

    # それぞれ格納された変数をDBにinsertする
    insert_table = school.school_master(
        school_name = val_list[0],
        nearest_station = val_list[1],
        address = val_list[2],
        operating_hour = val_list[3],
        lesson_hour = val_list[4],
        distance_station = val_list[5],
        number_students = val_list[6],
        lesson_time = val_list[7],
        numbers_of_lesson = val_list[8],
        price_minutes = val_list[9],
        price_month = val_list[10])
    session.add(insert_table)
    session.commit()
        
    return render_template(
        "confirmation_school_info.html",
        insert_table=insert_table)

# top.htmlを反映させるための関数
@app.route('/top')
def top():
  return render_template('top.html')

if __name__ == "__main__":
    app.run(debug=True)
