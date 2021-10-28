
# school_name = "有井教室"
# station = "岩本町"
# address = "千代田区岩本町"

# sql3 = "insert into school_master(school_name,"+\
#                                 "station,"+\
#                                 "address) "+\
#                                 "values(school_name = '%s',"  % (school_name)+\
#                                 "sation = '%s')" % (station)
# name = "a"

# sql = "SELECT * FROM hogehoge WHERE name = '%s'" % (name,)

# sql2 = (school_name, station)
# print(sql3)

# from flask import Flask,render_template,request
# import psycopg2

# +++

import psycopg2

path = "localhost"
port = "5432"
dbname = "testdb"
user = "ariikeisuke"
password = "candy1225"
conText = "host={} port={} dbname={} user={} password={}"
conText = conText.format(path,port,dbname,user,password)
connection = psycopg2.connect(conText)
cur = connection.cursor()


unique_school_id = "30"
school_name = 'kei'
nearest_station = "岩本町駅"
address = "千代田区岩本町"
operating_hour = "20"
lesson_hour = "30"
distance_station = "5"
number_students = "100"
lesson_time = "100"
numbers_of_lesson = "111"
price_minutes = "110"
price_month = "112"


sql = "insert into school_master(unique_school_id,"+\
                                    "school_name,"+\
                                    "nearest_station,"+\
                                    "address,"+\
                                    "operating_hour,"+\
                                    "lesson_hour,"+\
                                    "distance_station,"+\
                                    "number_students,"+\
                                    "lesson_time,"+\
                                    "numbers_of_lesson,"+\
                                    "price_minutes,"+\
                                    "price_month) "+\
                                    "values(%s," % (unique_school_id)+\
                                    "'%s'," % (school_name)+\
                                    "'%s'," % (nearest_station)+\
                                    "'%s'," % (address)+\
                                    "%s," % (operating_hour)+\
                                    "%s," % (lesson_hour)+\
                                    "%s," % (distance_station)+\
                                    "%s," % (number_students)+\
                                    "%s," % (lesson_time)+\
                                    "%s," % (numbers_of_lesson)+\
                                    "%s," % (price_minutes)+\
                                    "%s);" % (price_month)


cur.execute(sql)
connection.commit()
