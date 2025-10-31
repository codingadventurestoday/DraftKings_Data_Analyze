import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

secret_db_password = os.getenv("secret_db_password")
secret_db_name = os.getenv("secret_db_name")
secret_db_user = os.getenv("user")
secret_db_host = os.getenv("host")

def sql_data(operation):


    try:
        # 1. Create the connection engine
        connection_str = f"mysql+pymysql://{secret_db_user}:{secret_db_password}@{secret_db_host}/{secret_db_name}"
        engine = create_engine(connection_str)


        if operation == "store":
            df_to_write = pd.DataFrame()
    
            print("DataFrame to be written:")
            print(df_to_write)

            # 3. Define the table name
            table_name = ""

            # 4. Write DataFrame to MySQL table
            # if_exists='replace': If 'products' table exists, drop it and create a new one.
            # index=False: Don't write the pandas index as a column.
            df_to_write.to_sql(
                name=table_name,
                con=engine,
                index=False
            )
        elif operation == "get":
            query = "SELECT * FROM your_table_name"

            # 3. Read data into a DataFrame
            # This function runs the query and loads the results directly.
            df = pd.read_sql(query, engine)

            # Now 'df' is a pandas DataFrame
            print(df.head())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
    # 5. Clean up the engine connection
        if 'engine' in locals():
            engine.dispose()