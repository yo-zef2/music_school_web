from itertools import count
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
from .SchoolInfoJapan import SchoolInforJapan

class SchoolInfoJapanRepository:

    def find_by_area(self, address):

        "エリアごとにSchoolMasterから情報を取得する"

        school_info_by_area = Database.session.query(
            SchoolInforJapan).filter(
                SchoolInforJapan.address.like(
                    "{address}%".format(**{"address" : address}))).first()

        school_market_info = dict(
            school_id_web = school_info_by_area.school_id_web,
            address = school_info_by_area.address,
            count_school_num = school_info_by_area.count_school_num,
            average_price = school_info_by_area.average_price,
            max_price = school_info_by_area.max_price,
            min_price = school_info_by_area
        )
        return school_market_info
        
        # school_market_info = []
        # for school_info in school_info_by_area:
        #     unique_school_info = []
        #     unique_school_info.append(school_info.school_id_web)
        #     unique_school_info.append(school_info.address)
        #     unique_school_info.append(school_info.count_school_num)
        #     unique_school_info.append(school_info.average_price)
        #     unique_school_info.append(school_info.max_price)
        #     unique_school_info.append(school_info.min_price)
        #     school_market_info.append(unique_school_info)
        # school_info_by_area = pd.DataFrame(school_market_info)
        # print(school_info_by_area)
        # return school_info_by_area

    #    school_info_by_id = Database.session.query(
    #         SchoolMaster).filter(
    #             SchoolMaster.unique_school_id == school_id).first()
        # school_info = dict(
        #     unique_school_id = school_info_by_id.unique_school_id,
        #     school_name = school_info_by_id.school_name,
        #     nearest_station = school_info_by_id.nearest_station,
        #     address = school_info_by_id.address,
        #     operating_hour = school_info_by_id.operating_hour,
        #     lesson_hour = school_info_by_id.lesson_hour,
        #     distance_station = school_info_by_id.distance_station,
        #     number_students = school_info_by_id.number_students,
        #     lesson_time = school_info_by_id.lesson_time,
        #     numbers_of_lesson = school_info_by_id.numbers_of_lesson,
        #     price_minutes = school_info_by_id.price_minutes,
        #     price_month = school_info_by_id.price_month)
        # print(school_info)
        # return school_info