import os 
import sys
from src.mlproject.exception import CustomerException
from src.mlproject.logger import logging
import pymysql 
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pandas as pd   
from dotenv import load_dotenv
import pickle

load_dotenv()

host=os.getenv("host") 
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")



def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
             host=host,
             user=user,
             password=password,  # type: ignore
             db=db
        )

        logging.info("connection establish",mydb)

        df=pd.read_sql_query('Select * from raw',mydb)
        print(df.head())

        return df

    except Exception as ex:
        raise CustomerException(ex, sys) 