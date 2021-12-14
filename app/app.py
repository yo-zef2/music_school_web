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
from . import school
from . import database
from . import feature_value
from . import method
from . import question_self
from . import student_master_info

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

@app.route('/student_master_form',methods=["post"])
def get_student_master():
    school_name = request.form["school_name"]
    print(school_name)
    return render_template('student_master_form.html', school_name = school_name)

@app.route('/predict_price_form',methods=["post"])
def show_predict_price():
    unique_school_id = request.form["unique_school_id"]
    print(unique_school_id)
    return render_template('predict_price_form.html',unique_school_id = unique_school_id)

@app.route('/addadd',methods=["post"])
def post_price_predict():
    features = feature_value.feature(
        unique_school_id = request.form.get("unique_school_id"),
        coaching_history = request.form.get("coaching_history"),
        t_childminder = method.get_boolean(request.form.get("t_childminder")),
        t_kindergarden_teacher = method.get_boolean(request.form.get("t_kindergarden_teacher")),
        t_vocal_music = method.get_boolean(request.form.get("t_vocal_music")),
        t_beginner = method.get_boolean(request.form.get("t_beginner")),
        t_contest = method.get_boolean(request.form.get("t_contest")),
        former_university = request.form.get("former_university"),
        composition = method.get_boolean(request.form.get("composition")),
        study_abroad = method.get_boolean(request.form.get("study_abroad")))
    
    database.session.add(features)
    database.session.commit()

    return render_template('confirmation_feature_value.html',features = features)

@app.route('/motivation_assessment_form',methods=["post"])
def motivation_assessment():
    # ここにchange_data_type_student_masterを入れ込む
        student_info = student_master_info.change_data_type_student_master(
        student_name = request.form.get("student_name"),
        school_name = request.form.get("school_name"),
        student_age = request.form.get("student_age"),
        family_structure = request.form.get("family_structure"),
        student_address = request.form.get("student_address"),
        playing_history = request.form.get("playing_history"),
        learning_history = request.form.get("learning_history"),
        performance_level = request.form.get("performance_level"),
        achivement_homework = request.form.get("achivement_homework"),
        purpose_lesson = request.form.get("purpose_lesson"),
        participation_consert = request.form.get("participation_consert"))
        
        database.session.add(student_info)
        database.session.commit()
        
        return render_template('motivation_assessment_form.html', student_info = student_info)

@app.route('/confirm_question_self',methods=["post"])
def post_self_question():
    self_answer = question_self.change_data_type_self(
    unique_student_id = request.form.get("unique_student_id"),
    student_name = request.form.get("student_name"),
    reason_a_1 = method.get_int(request.form.get("reason_a_1")),
    reason_b_2 = method.get_int(request.form.get("reason_b_2")),
    reason_c_3 = method.get_int(request.form.get("reason_c_3")),
    reason_d_4 = method.get_int(request.form.get("reason_d_4")),
    reason_e_5 = method.get_int(request.form.get("reason_e_5")),
    reason_f_6 = method.get_int(request.form.get("reason_f_6")),
    reason_g_7 = method.get_int(request.form.get("reason_g_7")),
    reason_h_8 = method.get_int(request.form.get("reason_h_8")),
    reason_i_9 = method.get_int(request.form.get("reason_i_9")),
    reason_j_10 = method.get_int(request.form.get("reason_j_10")),
    reason_k_11 = method.get_int(request.form.get("reason_k_11")),
    reason_l_12 = method.get_int(request.form.get("reason_l_12")),
    reason_m_13 = method.get_int(request.form.get("reason_m_13")),
    reason_n_14 = method.get_int(request.form.get("reason_n_14")),
    reason_o_15 = method.get_int(request.form.get("reason_o_15")))

    print(type(self_answer.reason_a_1))
    database.session.add(self_answer)
    database.session.commit()

    return render_template('confirmation_self_answer.html',self_answer = self_answer)

if __name__ == "__main__":
    app.run(debug=True)
