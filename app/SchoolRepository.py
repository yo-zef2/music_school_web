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
from .SchoolMaster import SchoolMaster


class SchoolRepository:

    " SchoolMasterのCRUD操作"

    def insert_data(self,school_info):
        
        "SchoolMasterへのデータインサート"

        Database.session.add(school_info)
        Database.session.commit()

    def find_by_id(self,school_id):

        "IDでSchoolMasterから情報を取得する"

        school_info_by_id = Database.session.query(
            SchoolMaster).filter(
                SchoolMaster.unique_school_id == school_id).first()

        print(school_info_by_id)

        school_info = dict(
            unique_school_id = school_info_by_id.unique_school_id,
            school_name = school_info_by_id.school_name,
            nearest_station = school_info_by_id.nearest_station,
            address = school_info_by_id.address,
            operating_hour = school_info_by_id.operating_hour,
            lesson_hour = school_info_by_id.lesson_hour,
            distance_station = school_info_by_id.distance_station,
            number_students = school_info_by_id.number_students,
            lesson_time = school_info_by_id.lesson_time,
            numbers_of_lesson = school_info_by_id.numbers_of_lesson,
            price_minutes = school_info_by_id.price_minutes,
            price_month = school_info_by_id.price_month)
        print(school_info)
        return school_info

    def find_by_area(self, address):

        "エリアごとにSchoolMasterから情報を取得する"

        school_info_by_area = Database.session.query(
            SchoolMaster).filter(
                SchoolMaster.address.like(
                    "{address}%".format(**{"address" : address}))).all()
        school_info_list = []
        for school_info in school_info_by_area:
            unique_school_info = []
            unique_school_info.append(school_info.unique_school_id)
            unique_school_info.append(school_info.school_name)
            unique_school_info.append(school_info.nearest_station)
            unique_school_info.append(school_info.address)
            unique_school_info.append(school_info.operating_hour)
            unique_school_info.append(school_info.lesson_hour)
            unique_school_info.append(school_info.distance_station)
            unique_school_info.append(school_info.number_students)
            unique_school_info.append(school_info.lesson_time)
            unique_school_info.append(school_info.numbers_of_lesson)
            unique_school_info.append(school_info.price_minutes)
            unique_school_info.append(school_info.price_month)
            school_info_list.append(unique_school_info)
        school_info_by_area = pd.DataFrame(school_info_list)
        print(school_info_by_area)
        return school_info_by_area
