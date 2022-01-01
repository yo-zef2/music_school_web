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
from .FeatureValue import FeatureValue

class FeatureValueRepository:

    "FeatureValueのCRUD操作"

    def insert_data(self,features):
        
        "FeatureValueへのデータインサート"

        Database.session.add(features)
        Database.session.commit()

    def find_by_id(self,school_id):

        "IDでFeatureValueから情報を取得する"

        features_by_id = Database.session.query(
            FeatureValue).filter(
                FeatureValue.unique_school_id == school_id).first()
        features = dict(
            unique_school_id = features_by_id.unique_school_id,
            coaching_history = features_by_id.coaching_history,
            t_childminder = features_by_id.t_childminder,
            t_kindergarden_teacher = features_by_id.t_kindergarden_teacher,
            t_vocal_music = features_by_id.t_vocal_music,
            t_beginner = features_by_id.t_beginner,
            t_contest = features_by_id.t_contest,
            former_university = features_by_id.former_university,
            composition = features_by_id.composition,
            study_abroad = features_by_id.study_abroad,)
        print(features)
        return features


    # def find_by_area(self, address):

    #     "エリアごとにFeatureValueから情報を取得する"

    #     features_by_area = Database.session.query(
    #         FeatureValue).filter(
    #             FeatureValue.address.like(
    #                 "{address}%".format(**{"address" : address}))).all()
    #     features_list = []
    #     for features in features_by_area:
    #         unique_features = []
    #         unique_features.append(features.unique_school_id)
    #         unique_features.append(features.school_name)
    #         unique_features.append(features.nearest_station)
    #         unique_features.append(features.address)
    #         unique_features.append(features.operating_hour)
    #         unique_features.append(features.lesson_hour)
    #         unique_features.append(features.distance_station)
    #         unique_features.append(features.number_students)
    #         unique_features.append(features.lesson_time)
    #         unique_features.append(features.numbers_of_lesson)
    #         unique_features.append(features.price_minutes)
    #         unique_features.append(features.price_month)
    #         features_list.append(unique_features)
    #     features_by_area = pd.DataFrame(features_list)
    #     print(features_by_area)
    #     return features_by_area
