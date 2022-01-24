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
from .SchoolMaster import SchoolMaster
from . import Database
from .FeatureValue import FeatureValue
from . import Method
from .QuestionSelf import QuestionSelf
from .QuestionFact import QuestionFact
from .StudentMaster import StudentMaster
from .SchoolRepository import SchoolRepository
from .StudentRepository import StudentRepository
from .QusetionSelfRepository import QuestionSelfRepository
from .QuestionFactRepository import QuestionFactRepository
from .FeatureValueRepository import FeatureValueRepository

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
    insert_table = SchoolMaster(
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
    repository = SchoolRepository()
    repository.insert_data(insert_table) # データの格納
    return render_template(
        "confirmation_school_info.html",
        insert_table=insert_table)

# # SchoolMasterのCRUD操作のテスト用

# repository = SchoolRepository()
# repository.find_by_area("千代田区")

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
    features = FeatureValue(
        unique_school_id = request.form.get("unique_school_id"),
        coaching_history = request.form.get("coaching_history"),
        t_childminder = Method.get_boolean(request.form.get("t_childminder")),
        t_kindergarden_teacher = Method.get_boolean(request.form.get("t_kindergarden_teacher")),
        t_vocal_music = Method.get_boolean(request.form.get("t_vocal_music")),
        t_beginner = Method.get_boolean(request.form.get("t_beginner")),
        t_contest = Method.get_boolean(request.form.get("t_contest")),
        former_university = request.form.get("former_university"),
        composition = Method.get_boolean(request.form.get("composition")),
        study_abroad = Method.get_boolean(request.form.get("study_abroad")))

    repository = FeatureValueRepository()
    repository.insert_data(features)
    school_repository = SchoolRepository()
    school_master = school_repository.find_by_id(features.unique_school_id)
    print(school_master)
    return render_template('confirmation_feature_value.html',features = features, school_master=school_master)

# # FeatureValueのCRUD操作のテスト用

# repository = FeatureValueRepository()
# repository.find_by_id(339)

@app.route('/motivation_assessment_form',methods=["post"])
def motivation_assessment():
    # ここにchange_data_type_student_masterを入れ込む
        student_info = StudentMaster(
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
        
        repository = StudentRepository()
        repository.insert_data(student_info) # データの格納

        return render_template('motivation_assessment_form.html', student_info = student_info)


# # StudentMasterのCRUD操作のテスト用

# repository = StudentRepository()
# repository.find_by_id(5)


@app.route('/confirm_question_self',methods=["post"])
def post_self_question():
    self_answer = QuestionSelf(
    unique_student_id = request.form.get("unique_student_id"),
    student_name = request.form.get("student_name"),
    reason_a_1 = Method.get_int(request.form.get("reason_a_1")),
    reason_b_2 = Method.get_int(request.form.get("reason_b_2")),
    reason_c_3 = Method.get_int(request.form.get("reason_c_3")),
    reason_d_4 = Method.get_int(request.form.get("reason_d_4")),
    reason_e_5 = Method.get_int(request.form.get("reason_e_5")),
    reason_f_6 = Method.get_int(request.form.get("reason_f_6")),
    reason_g_7 = Method.get_int(request.form.get("reason_g_7")),
    reason_h_8 = Method.get_int(request.form.get("reason_h_8")),
    reason_i_9 = Method.get_int(request.form.get("reason_i_9")),
    reason_j_10 = Method.get_int(request.form.get("reason_j_10")),
    reason_k_11 = Method.get_int(request.form.get("reason_k_11")),
    reason_l_12 = Method.get_int(request.form.get("reason_l_12")),
    reason_m_13 = Method.get_int(request.form.get("reason_m_13")),
    reason_n_14 = Method.get_int(request.form.get("reason_n_14")),
    reason_o_15 = Method.get_int(request.form.get("reason_o_15")))

    repository = QuestionSelfRepository()
    repository.insert_data(self_answer)

    factor_answer = QuestionFact(
    unique_student_id = request.form.get("unique_student_id"),
    student_name = request.form.get("student_name"),
    question_b9_1 = request.form.get("question_b9_1"),
    question_c11_1 = Method.get_int(request.form.get("question_c11_1")),
    question_c11_2 = Method.get_int(request.form.get("question_c11_2")),
    question_c11_3 = Method.get_int(request.form.get("question_c11_3")),
    question_c11_4 = Method.get_int(request.form.get("question_c11_4")),
    question_c11_5 = Method.get_int(request.form.get("question_c11_5")),
    question_c11_6 = Method.get_int(request.form.get("question_c11_6")),
    question_d12_1 = Method.get_int(request.form.get("question_d12_1")),
    question_d12_2 = Method.get_int(request.form.get("question_d12_2")),
    question_d12_3 = Method.get_int(request.form.get("question_d12_3")),
    question_d12_4 = Method.get_int(request.form.get("question_d12_4")),
    question_d12_5 = Method.get_int(request.form.get("question_d12_5")),
    question_d12_6 = Method.get_int(request.form.get("question_d12_6")),
    question_e13_1 = Method.get_int(request.form.get("question_e13_1")),
    question_e13_2 = Method.get_int(request.form.get("question_e13_2")),
    question_e13_3 = Method.get_int(request.form.get("question_e13_3")),
    question_e13_4 = Method.get_int(request.form.get("question_e13_4")),
    question_e13_5 = Method.get_int(request.form.get("question_e13_5")),
    question_e13_6 = Method.get_int(request.form.get("question_e13_6")),
    question_f14_1 = Method.get_int(request.form.get("question_f14_1")),
    question_f14_2 = Method.get_int(request.form.get("question_f14_2")),
    question_f14_3 = Method.get_int(request.form.get("question_f14_3")),
    question_f14_4 = Method.get_int(request.form.get("question_f14_4")),
    question_f14_5 = Method.get_int(request.form.get("question_f14_5")),
    question_f14_6 = Method.get_int(request.form.get("question_f14_6")),
    question_f14_7 = Method.get_int(request.form.get("question_f14_7")),
    question_g15_1 = Method.get_int(request.form.get("question_g15_1")),
    question_g15_2 = Method.get_int(request.form.get("question_g15_2")),
    question_g15_3 = Method.get_int(request.form.get("question_g15_3")),
    question_g15_4 = Method.get_int(request.form.get("question_g15_4")))

    repository = QuestionFactRepository()
    repository.insert_data(factor_answer)

    return render_template(
        'confirmation_self_answer.html',
        self_answer = self_answer,
        factor_answer = factor_answer)

# # QuestionSelfのCRUD操作のテスト用

# repository = QuestionSelfRepository()
# repository.find_by_id(11)

# # QuestionFactのCRUD操作のテスト用

# repository = QuestionFactRepository()
# repository.find_by_id(11)

if __name__ == "__main__":
    app.run(debug=True)
