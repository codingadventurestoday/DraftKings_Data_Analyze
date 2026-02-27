from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd

from get_information.data_mysql import get_data


y_true = ""
y_pred = ""

mse = mean_squared_error(y_true, y_pred)