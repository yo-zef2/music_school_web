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
from . import school
from . import database
from . import feature_value

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    instruments = ["ピアノ","ギター","ベース","ドラム"]
    return render_template("index.html",name=name,instruments=instruments)

@app.route("/add",methods=["post"])
def post():
    # Webページで記入された内容を変数に格納する
    insert_table = school.school_master(
        school_name = request.form["school_name"],
        nearest_station = request.form["station"],
        address = request.form["address"],
        operating_hour = request.form["operating_hour"],
        lesson_hour = request.form["lesson_hour"],
        distance_station = request.form["distance"],
        number_students = request.form["number_student"],
        lesson_time = request.form["lesson_time"],
        numbers_of_lesson = request.form["numbers_of_lesson"],
        price_minutes = request.form["price_minutes"],
        price_month = request.form["price_month"])
    database.session.add(insert_table)
    database.session.commit()

    return render_template(
        "confirmation_school_info.html",
        insert_table=insert_table)

# top.htmlを反映させるための関数
@app.route('/top')
def top():
  return render_template('top.html')

@app.route('/predict_price_form')
def show_predict_price():
    return render_template('predict_price_form.html')

@app.route('/addadd',methods=["post"])
def post_price_predict():
    unique_school_id = request.form.get("unique_school_id")
    coaching_history = request.form.get("coaching_history")
    t_childminder = request.form.get("t_childminder")
    t_kindergarden_teacher = request.form.get("t_kindergarden_teacher")
    t_vocal_music = request.form.get("t_vocal_music")
    t_beginner = request.form.get("t_beginner")
    t_contest = request.form.get("t_contest")
    former_university = request.form.get("former_university")
    composition = request.form.get("composition")
    study_abroad = request.form.get("study_abroad")
    
    # NoneをFalseに変換する処理をする

    val_list = [
        unique_school_id,
        coaching_history,
        t_childminder,
        t_kindergarden_teacher,
        t_vocal_music,
        t_beginner,
        t_contest,
        former_university,
        composition,
        study_abroad]
        
    for i in range(len(val_list)):
        if val_list[i] == None:
            val_list[i] = False
        elif val_list[i] == "True":
            val_list[i] = True

    features = feature_value.feature(
        unique_school_id = val_list[0],
        coaching_history = val_list[1],
        t_childminder = val_list[2],
        t_kindergarden_teacher = val_list[3],
        t_vocal_music = val_list[4],
        t_beginner = val_list[5],
        t_contest = val_list[6],
        former_university = val_list[7],
        composition = val_list[8],
        study_abroad = val_list[9])

    database.session.add(features)
    database.session.commit()
    
    return render_template('testtest.html',features = features)

@app.route('/motivation_assessment_form')
def motivation_assessment():
  return render_template('motivation_assessment_form.html')

if __name__ == "__main__":
    app.run(debug=True)

