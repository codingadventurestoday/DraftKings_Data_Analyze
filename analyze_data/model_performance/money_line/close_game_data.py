import pandas as pd

from get_information.data_mysql import get_data
from analyze_data.model_performance.create_metrics.classification_report import make_classification_report

query = """SELECT
                g.gameID, g.score_home,
                g.score_away, 
                o.oddsID, 
                o.home_spread,
                 
            FROM games g 
            INNER JOIN odds o ON o.gameID = g.gameID
            WHERE ABS(o.home_spread) <= 7;"""

df = get_data(query)

df["margin"] = df["score_home"] - df["score_away"]
df["actual_cover"] = (df["margin"] + df["home_spread"] > 0).astype(int)

# might be able to modify 0 to find categories
df["predicted_cover"] = (df["home_spread"] < 0).astype(int)

polling = (
    df.groupby("gameID")
      .agg(
          actual_cover=("actual_cover", "first"),
          votes_for_home=("predicted_cover", "sum"),
          total_votes=("predicted_cover", "count")
      )
)

polling["predicted_cover"] = (
    polling["votes_for_home"] > (polling["total_votes"] / 2)
).astype(int)


# data for all games 
all_report = make_classification_report(polling["actual_cover"], polling["predicted_cover"])

print("accuracy: ", all_report.precison)