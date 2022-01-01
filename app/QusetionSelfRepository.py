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
from .QuestionSelf import QuestionSelf

class QuestionSelfRepository:

    " QuestionSelfのCRUD操作"

    def insert_data(self,self_answer):
        
        "QuestionSelfへのデータインサート"

        Database.session.add(self_answer)
        Database.session.commit()

    def find_by_id(self,student_id):

        "IDでQuestionSelfRepositoryから情報を取得する"

        self_answer_by_id = Database.session.query(
            QuestionSelf).filter(
                QuestionSelf.unique_student_id == student_id).first()
        self_answer = dict(
            unique_student_id = self_answer_by_id.unique_student_id,
            student_name = self_answer_by_id.student_name,
            reason_a_1 = self_answer_by_id.reason_a_1,
            reason_b_2 = self_answer_by_id.reason_b_2,
            reason_c_3 = self_answer_by_id.reason_c_3,
            reason_d_4 = self_answer_by_id.reason_d_4,
            reason_e_5 = self_answer_by_id.reason_e_5,
            reason_f_6 = self_answer_by_id.reason_f_6,
            reason_g_7 = self_answer_by_id.reason_g_7,
            reason_h_8 = self_answer_by_id.reason_h_8,
            reason_i_9 = self_answer_by_id.reason_i_9,
            reason_j_10 = self_answer_by_id.reason_j_10)
        print(self_answer)
        return self_answer


    # def find_by_area(self, address):

    #     "エリアごとにStudentMasterから情報を取得する"

    #     self_answer_by_area = Database.session.query(
    #         QuestionSelf).filter(
    #             QuestionSelf.student_address.like(
    #                 "{address}%".format(**{"address" : address}))).all()
    #     self_answer_list = []
    #     for self_answer in self_answer_by_area:
    #         unique_self_answer = []
    #         unique_self_answer.append(self_answer.unique_student_id)
    #         unique_self_answer.append(self_answer.student_name)
    #         unique_self_answer.append(self_answer.school_name)
    #         unique_self_answer.append(self_answer.student_age)
    #         unique_self_answer.append(self_answer.family_structure)
    #         unique_self_answer.append(self_answer.student_address)
    #         unique_self_answer.append(self_answer.learning_history)
    #         unique_self_answer.append(self_answer.performance_level)
    #         unique_self_answer.append(self_answer.achivement_homework)
    #         unique_self_answer.append(self_answer.purpose_lesson)
    #         unique_self_answer.append(self_answer.participation_consert)
    #         self_answer_list.append(unique_self_answer)
    #     self_answer_by_area = pd.DataFrame(self_answer_list)
    #     print(self_answer_by_area)
    #     return self_answer_by_area
