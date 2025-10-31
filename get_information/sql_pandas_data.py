from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

secret_db_password = os.getenv("secret_db_password")
secret_db_name = os.getenv("secret_db_name")
secret_db_user = os.getenv("user")
secret_db_host = os.getenv("host")

def sql_data(operation):
    try:
        connection_str = f"mysql+pymysql://{secret_db_user}:{secret_db_password}@{secret_db_host}/{secret_db_name}"
        engine = create_engine(connection_str)


    except Exception as e:
        print(f"An error occurred: {e}")

    return engine