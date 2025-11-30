import pandas as pd

from sql_pandas_data import get_sql_engine

def get_data(query_string, params=None):
    engine = get_sql_engine()
    
    if engine is None:
          return None

    try:
        df = pd.read_sql(query_string, engine, params=params)
        return df

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
         engine.dispose()