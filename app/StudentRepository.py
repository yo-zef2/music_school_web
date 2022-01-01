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
from .StudentMaster import StudentMaster

class StudentRepository:

    " StudentMasterのCRUD操作"

    def insert_data(self,student_info):
        
        "StudentMasterへのデータインサート"

        Database.session.add(student_info)
        Database.session.commit()

    def find_by_id(self,Student_id):

        "IDでStudentMasterから情報を取得する"

        student_info_by_id = Database.session.query(
            StudentMaster).filter(
                StudentMaster.unique_student_id == Student_id).first()
        student_info = dict(
            unique_student_id = student_info_by_id.unique_student_id,
            student_name = student_info_by_id.student_name,
            school_name = student_info_by_id.school_name,
            student_age = student_info_by_id.student_age,
            family_structure = student_info_by_id.family_structure,
            student_address = student_info_by_id.student_address,
            learning_history = student_info_by_id.learning_history,
            performance_level = student_info_by_id.performance_level,
            achivement_homework = student_info_by_id.achivement_homework,
            purpose_lesson = student_info_by_id.purpose_lesson,
            participation_consert = student_info_by_id.participation_consert)
        print(student_info)
        return student_info

    def find_by_area(self, address):

        "エリアごとにStudentMasterから情報を取得する"

        student_info_by_area = Database.session.query(
            StudentMaster).filter(
                StudentMaster.student_address.like(
                    "{address}%".format(**{"address" : address}))).all()
        student_info_list = []
        for student_info in student_info_by_area:
            unique_student_info = []
            unique_student_info.append(student_info.unique_student_id)
            unique_student_info.append(student_info.student_name)
            unique_student_info.append(student_info.school_name)
            unique_student_info.append(student_info.student_age)
            unique_student_info.append(student_info.family_structure)
            unique_student_info.append(student_info.student_address)
            unique_student_info.append(student_info.learning_history)
            unique_student_info.append(student_info.performance_level)
            unique_student_info.append(student_info.achivement_homework)
            unique_student_info.append(student_info.purpose_lesson)
            unique_student_info.append(student_info.participation_consert)
            student_info_list.append(unique_student_info)
        student_info_by_area = pd.DataFrame(student_info_list)
        print(student_info_by_area)
        return student_info_by_area
