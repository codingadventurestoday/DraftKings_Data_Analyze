import pandas as pd

from sql_pandas_data import sql_data


engine = sql_data()

def store_data(table_name):
    df_to_write = pd.DataFrame()

    df_to_write.to_sql(
        name=table_name,
        con=engine,
        index=False
    )

    if 'engine' in locals():
            engine.dispose()