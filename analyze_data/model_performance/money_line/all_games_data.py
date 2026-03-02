import pandas as pd
import numpy as np

from get_information.data_mysql import get_data
from analyze_data.model_performance.create_metrics.classification_report import make_classification_report

query = """SELECT 
    g.gameID, 
    g.score_home, 
    g.score_away, 
    o.home_moneyline, 
    o.away_moneyline
FROM games g
INNER JOIN odds o 
    ON g.gameID = o.gameID;"""


df = get_data(query)

# 1 = home; 0 = away

df["margin"] = df["score_away"] - df["score_home"]

df["actual_winner"] = np.where(
    df["margin"] > 0, 0,
    np.where(df["margin"] < 0, 1, -1)
)

df["snapshot_pred"] = np.where(df["home_moneyline"] < 0, 1, 0)

polling = (
    df.groupby("gameID")["snapshot_pred"]
      .mean()
      .reset_index()
)

polling["predicted_winner"] = (polling["snapshot_pred"] > 0.5).astype(int)

game_results = df[["gameID", "actual_winner"]].drop_duplicates()

final_df = game_results.merge(
    polling[["gameID", "predicted_winner"]],
    on="gameID"
)
final_df["correct_prediction"] = (final_df["predicted_winner"] == final_df["actual_winner"]).astype(int)
final_df.loc[final_df["actual_winner"] == -1, "correct_prediction"] = 0

# we need to ensure that the column data types are same for putting into metric equations
y_true = final_df["actual_winner"].replace(-1,0)

y_pred = final_df["predicted_winner"]

# data for all games 
all_report = make_classification_report(y_true, y_pred)

print("Accuracy: ", all_report.accuracy)
print("Precision: ", all_report.precison)
print("Recall: ", all_report.recall)
print("F1: ", all_report.f1)