import pandas as pd
from sqlalchemy import create_engine

# --- Configuration ---
user = 'root'
password = 'mypassword123'
host = '127.0.0.1'
db_name = 'sales_db'
# ---------------------

try:
    # 1. Create the connection engine
    connection_str = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
    engine = create_engine(connection_str)

    # 2. Create a sample DataFrame
    data = {
        'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics'],
        'price': [1200, 40, 100, 350]
    }
    df_to_write = pd.DataFrame(data)
    
    print("DataFrame to be written:")
    print(df_to_write)

    # 3. Define the table name
    table_name = 'products'

    # 4. Write DataFrame to MySQL table
    # if_exists='replace': If 'products' table exists, drop it and create a new one.
    # index=False: Don't write the pandas index as a column.
    df_to_write.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',
        index=False
    )
    
    print(f"\nSuccessfully wrote data to MySQL table '{table_name}'.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 5. Clean up the engine connection
    if 'engine' in locals():
        engine.dispose()