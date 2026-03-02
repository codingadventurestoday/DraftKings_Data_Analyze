import pandas as pd

from get_information.data_mysql import get_data
from analyze_data.model_performance.create_metrics.classification_report import make_classification_report

query = """SELECT
                g.gameID, g.score_home,
                g.score_away, 
                o.oddsID, 
                o.home_spread 
            FROM games g 
            INNER JOIN odds o ON o.gameID = g.gameID
            WHERE ABS(o.home_spread) > 8
            AND ABS(o.home_spread) <= 16;"""

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

# data where game is predicted to be competivite   9>= x <= 16
#comp_report = make_classification_report(df[""], df[""])

print("accuracy: ", all_report.accuracy)
print("precision: ", all_report.precison)
print("recall: ", all_report.recall)
print("f1: ", all_report.f1)

"""
this spread occurred in just 40 games
40% accuracy for competitive games (spreads 8-16).

Market Inefficiency: In a perfectly efficient market, this should be near 50%. A 40% accuracy rate suggests that in games where DraftKings expects a clear favorite (but not a blowout), the underdog is actually covering the spread much more often than the market predicts.
"""