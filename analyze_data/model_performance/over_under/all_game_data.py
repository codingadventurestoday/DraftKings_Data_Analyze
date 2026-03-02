import pandas as pd

from get_information.data_mysql import get_data
from analyze_data.model_performance.create_metrics.regression_metrics import regression_metrics

query = """SELECT 
            o.gameID, 
            AVG(o.over_under) AS avg_over_under, 
            (g.score_home + g.score_away) AS total_score
        FROM odds o
        INNER JOIN games g ON o.gameID = g.gameID
        GROUP BY g.gameID;"""


df = get_data(query)

y_pred, y_true = df['avg_over_under'], df['total_score']

# mae, rmse, r2
report = regression_metrics(y_true, y_pred)

print(report.mae)
print(report.rmse)
print(report.r2)