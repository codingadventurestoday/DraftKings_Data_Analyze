import pandas as pd

from sql_pandas_data import sql_data


engine = sql_data()

def store_data(table_name):
    df_to_write = pd.DataFrame()
    
    print("DataFrame to be written:")
    print(df_to_write)

    # 3. Define the table name

    # 4. Write DataFrame to MySQL table
    # if_exists='replace': If 'products' table exists, drop it and create a new one.
    # index=False: Don't write the pandas index as a column.
    df_to_write.to_sql(
        name=table_name,
        con=engine,
        index=False
    )

    if 'engine' in locals():
            engine.dispose()