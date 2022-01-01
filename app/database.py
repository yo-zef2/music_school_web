from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import VARCHAR
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

db_url = ("{dialect}://{username}:{password}@{host}:{port}/{database}").format(
    **{'dialect': 'postgresql',
    'username': 'ariikeisuke',
    'password': 'candy1225',
    'host': 'localhost',
    'port': '5432',
    'database': 'testdb'})

engine = create_engine(db_url)
Base = declarative_base()
SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()

