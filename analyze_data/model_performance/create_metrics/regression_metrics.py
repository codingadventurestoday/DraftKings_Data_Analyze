from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, root_mean_squared_error
import pandas as pd


class regression:
    def __init__(self, mae, rmse, r2):
        self.mae = mae
        self.rmse = rmse
        self.r2 = r2

def regression_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    report = regression(mae, rmse, r2)
    return report