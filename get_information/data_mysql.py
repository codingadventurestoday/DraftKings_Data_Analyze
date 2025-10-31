import pandas as pd
from sqlalchemy import create_engine

# 1. Create the database engine
# Replace with your actual database credentials
user = 'your_username'
password = 'your_password'
host = 'localhost'       
db_name = 'your_database'

# This creates the connection string
connection_str = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

# Create the engine object
engine = create_engine(connection_str)

# 2. Define your SQL query
query = "SELECT * FROM your_table_name"

# 3. Read data into a DataFrame
# This function runs the query and loads the results directly.
df = pd.read_sql(query, engine)

# Now 'df' is a pandas DataFrame
print(df.head())


if 'engine' in locals():
        engine.dispose()