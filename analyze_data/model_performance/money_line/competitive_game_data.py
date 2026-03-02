import pandas as pd

from get_information.data_mysql import get_data
from analyze_data.model_performance.create_metrics.classification_report import make_classification_report

query = """SELECT 
            o.game_id, 
            AVG(o.over_under), 
            (g.score_home + g.score_away) AS total_score
        FROM odds o
        INNER JOIN games g ON o.game_id = g.game_id
        GROUP BY g.game_id;"""


df = get_data(query)

# data where game is predicted to be competivite   9>= x <= 16