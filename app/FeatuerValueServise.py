import pandas as pd
import numpy as np


class FeatureValueServise:

    def forecast_price(self, features):
        intercept = 59.24843864264586
        explanatory_variable = (intercept +
                            features.coaching_histtory*(-0.057814) +
                            features.t_childminder*(-2.629911) +
                            features.t_kindergarden_teacher*(-1.114511)+
                            features.t_vocal_music*(-0.475124)+
                            features.t_beginner*(2.028346)+
                            features.t_contest*(2.835193)+
                            features.toho_university*(11.601225)+
                            features.tokyo_university*(-0.535470)+
                            features.composition*(4.651286)+
                            features.study_abroad*(9.124657))


#    features = FeatureValue(
#         unique_school_id = request.form.get("unique_school_id"),
#         coaching_history = request.form.get("coaching_history"),
#         t_childminder = Method.get_boolean(request.form.get("t_childminder")),
#         t_kindergarden_teacher = Method.get_boolean(request.form.get("t_kindergarden_teacher")),
#         t_vocal_music = Method.get_boolean(request.form.get("t_vocal_music")),
#         t_beginner = Method.get_boolean(request.form.get("t_beginner")),
#         t_contest = Method.get_boolean(request.form.get("t_contest")),
#         former_university = request.form.get("former_university"),
#         composition = Method.get_boolean(request.form.get("composition")),
#         study_abroad = Method.get_boolean(request.form.get("study_abroad")))