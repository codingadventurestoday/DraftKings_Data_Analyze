import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv()

secret_db_password = os.getenv("secret_db_password")
secret_db_name = os.getenv("secret_db_name")
secret_db_user = os.getenv("user")
secret_db_host = os.getenv("host")



def connect_to_db():
    conn = mysql.connector.connect(
        host=secret_db_host,
        port=3306,
        user =secret_db_user,
        password = secret_db_password,
        database = secret_db_name,
    )

    print("reached connection successfully")

    return conn