from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
#this is the format of the URL to connect the database to the fast api shown below
#URL = "postgressql://<username>:<password>@<ip-address/hostname>/<database_name>"
SQL_ALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostame}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True: #just for reference as this code doesn't impact the API because now we r connected to the database using SQL alchemy, this code is used to connect to postgres directly
#     try:
#         conn = psycopg2.connect(host = "localhost",port = 5432, database = "fastapi", user = "postgres",password = "jigubhai007", cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print("Yayy")
#         break
#     except Exception as error:
#         print("Nooo Anakin!!!")
#         print("y did u do this:", error)
#         time.sleep(10)
