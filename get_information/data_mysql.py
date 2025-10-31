import pandas as pd

from sql_pandas_data import sql_data

engine = sql_data()

def get_data():
    query = "SELECT * FROM your_table_name"

    # 3. Read data into a DataFrame
    # This function runs the query and loads the results directly.
    df = pd.read_sql(query, engine)

    # Now 'df' is a pandas DataFrame
    print(df.head())

if 'engine' in locals():
            engine.dispose()