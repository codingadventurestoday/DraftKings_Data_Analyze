from analyze_data.explore_data.utils import plot_categorical_bar

from analyze_data.explore_data.explore_odds import fav_counts
from analyze_data.explore_data.explore_games import amount_home_wins, amount_away_wins

expected_away_wins = fav_counts['Away']
expected_home_wins = fav_counts['Home']

win_data = {
    'expected_away_wins' : expected_away_wins,
    'expected_home_wins' : expected_home_wins,
    'actual_home_wins' : amount_home_wins,
    'amount_away_wins' :  amount_away_wins
}

plot_categorical_bar(win_data, 'Predicted Wins vs Actual Wins based on Location')