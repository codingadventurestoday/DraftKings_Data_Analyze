import pandas as pd

from get_information.data_mysql import get_data
from analyze_data.model_performance.create_metrics.classification_report import make_classification_report

query = "SELECT g.gameID, g.score_home, g.score_away, o.oddsID, o.home_spread FROM games g INNER JOIN odds o ON o.gameID = g.gameID;"
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


print("accuracy: ", all_report.accuracy)
print("precision: ", all_report.precison)
print("recall: ", all_report.recall)
print("f1: ", all_report.f1)


"""
That is a crucial distinction. Since you are evaluating the DraftKings model (the market line) rather than a custom predictive model, these results are effectively an audit of Market Efficiency.

When the "Market" has an accuracy of 50.78%, it confirms that the oddsmakers have successfully reached "Equilibrium." They have set the lines so precisely that the outcome is essentially a random coin flip for the general public.

1. The Market Efficiency Audit
In a perfectly efficient market, every metric should hover right around 0.50. The fact that DraftKings is at 0.5078 shows they are doing their job perfectly: they've created a line where there is no easy "edge" for a bettor to exploit by simply following the spread.

2. The "Recall" Anomaly (0.592)
This is the most interesting piece of data in your audit. A Recall of 0.592 means the market is actually quite good at "capturing" the games where the home team covers.

Interpretation: If the home team is going to cover, the DraftKings line is "aware" of it nearly 60% of the time.

The "Precision" Trap (0.496): However, the market "over-calls" these covers. It predicts a home cover so often that it ends up being wrong more than half the time (Precision < 0.50).

This suggests a slight Home Field Bias in the market lines—the lines might be slightly shaded toward the home team to account for public betting patterns, 

"""