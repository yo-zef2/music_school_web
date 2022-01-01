from sqlalchemy import create_engine
import numpy as np 
import pandas as pd 
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from . import Database
from .QuestionFact import QuestionFact

class QuestionFactRepository:

    "QuestionFactのCRUD操作"

    def insert_data(self,fact_answer):
        
        "QuestionFactへのデータインサート"

        Database.session.add(fact_answer)
        Database.session.commit()

    def find_by_id(self,student_id):

        "IDでQuestionFactRepositoryから情報を取得する"

        fact_answer_by_id = Database.session.query(
            QuestionFact).filter(
                QuestionFact.unique_student_id == student_id).first()
        fact_answer = dict(
            unique_student_id = fact_answer_by_id.unique_student_id,
            student_name = fact_answer_by_id.student_name,
            question_b9_1 = fact_answer_by_id.question_b9_1,
            question_c11_1 = fact_answer_by_id.question_c11_1,
            question_c11_2 = fact_answer_by_id.question_c11_2,
            question_c11_3 = fact_answer_by_id.question_c11_3,
            question_c11_4 = fact_answer_by_id.question_c11_4,
            question_c11_5 = fact_answer_by_id.question_c11_5,
            question_c11_6 = fact_answer_by_id.question_c11_6,
            question_d12_1 = fact_answer_by_id.question_d12_1,
            question_d12_2 = fact_answer_by_id.question_d12_2,
            question_d12_3 = fact_answer_by_id.question_d12_3,
            question_d12_4 = fact_answer_by_id.question_d12_4,
            question_d12_5 = fact_answer_by_id.question_d12_5,
            question_d12_6 = fact_answer_by_id.question_d12_6,
            question_e13_1 = fact_answer_by_id.question_e13_1,
            question_e13_2 = fact_answer_by_id.question_e13_2,
            question_e13_3 = fact_answer_by_id.question_e13_3,
            question_e13_4 = fact_answer_by_id.question_e13_4,
            question_e13_5 = fact_answer_by_id.question_e13_5,
            question_e13_6 = fact_answer_by_id.question_e13_6,
            question_f14_1 = fact_answer_by_id.question_f14_1,
            question_f14_2 = fact_answer_by_id.question_f14_2,
            question_f14_3 = fact_answer_by_id.question_f14_3,
            question_f14_4 = fact_answer_by_id.question_f14_4,
            question_f14_5 = fact_answer_by_id.question_f14_5,
            question_f14_6 = fact_answer_by_id.question_f14_6,
            question_f14_7 = fact_answer_by_id.question_f14_7,
            question_g15_1 = fact_answer_by_id.question_g15_1,
            question_g15_2 = fact_answer_by_id.question_g15_2,
            question_g15_3 = fact_answer_by_id.question_g15_3,
            question_g15_4 = fact_answer_by_id.question_g15_4,
            )
        print(fact_answer)
        return fact_answer
    
    # def find_by_area(self, address):

    #     "エリアごとにStudentMasterから情報を取得する"

    #     fact_answer_by_area = Database.session.query(
    #         QuestionFact).filter(
    #             QuestionFact.student_address.like(
    #                 "{address}%".format(**{"address" : address}))).all()
    #     fact_answer_list = []
    #     for fact_answer in fact_answer_by_area:
    #         unique_fact_answer = []
    #         unique_fact_answer.append(fact_answer.unique_student_id)
    #         unique_fact_answer.append(fact_answer.student_name)
    #         unique_fact_answer.append(fact_answer.school_name)
    #         unique_fact_answer.append(fact_answer.student_age)
    #         unique_fact_answer.append(fact_answer.family_structure)
    #         unique_fact_answer.append(fact_answer.student_address)
    #         unique_fact_answer.append(fact_answer.learning_history)
    #         unique_fact_answer.append(fact_answer.performance_level)
    #         unique_fact_answer.append(fact_answer.achivement_homework)
    #         unique_fact_answer.append(fact_answer.purpose_lesson)
    #         unique_fact_answer.append(fact_answer.participation_consert)
    #         fact_answer_list.append(unique_fact_answer)
    #     fact_answer_by_area = pd.DataFrame(fact_answer_list)
    #     print(fact_answer_by_area)
    #     return fact_answer_by_area
