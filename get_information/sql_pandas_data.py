from sqlalchemy import create_engine

import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

secret_db_password = quote_plus(os.getenv("secret_db_password"))
secret_db_name = os.getenv("secret_db_name")
secret_db_user = os.getenv("user")
secret_db_host = os.getenv("host")

def get_sql_engine():
    engine = None
    
    connection_str = f"mysql+pymysql://{secret_db_user}:{secret_db_password}@{secret_db_host}/{secret_db_name}"
    engine = create_engine(connection_str)

    return engine