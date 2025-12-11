from analyze_data.explore_data.utils import plot_categorical_bar

from analyze_data.explore_data.explore_odds import total_projected_blow_outs, total_projected_competitive, total_projected_close
from analyze_data.explore_data.explore_games import amount_close_games, amount_blow_outs_games, amount_competitive_games

win_data = {
    'expected close' : total_projected_close,
    'expected competitive' : total_projected_competitive,
    'expected blow outs' : total_projected_blow_outs,
    'actual close' : amount_close_games,
    'actual competitive' : amount_competitive_games,
    'actual blow outs' :  amount_blow_outs_games
}

plot_categorical_bar(win_data, 'Predicted and Actual Game Types')