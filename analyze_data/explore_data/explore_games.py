from get_information.data_mysql import get_data
from analyze_data.explore_data import utils

"""run file from root dir: python3 -m analyze_data.explore_data.explore_games.py"""

"""
gameID SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
game_date DATE,
home_teamID TINYINT UNSIGNED,
away_teamID TINYINT UNSIGNED,
score_home TINYINT UNSIGNED,
score_away TINYINT UNSIGNED,
seasonID TINYINT UNSIGNED,
week TINYINT UNSIGNED,
FOREIGN KEY (home_teamID) REFERENCES teams(teamID),
FOREIGN KEY (away_teamID) REFERENCES teams(teamID),
FOREIGN KEY (seasonID) REFERENCES seasons(seasonID)
"""

game_data_query = 'SELECT gameID, score_home, score_away FROM games WHERE game_date <= NOW();'

game_data = get_data(game_data_query)

score_diff = (game_data['score_home'] - game_data['score_away']).abs()

"""How many games were blow outs"""
amount_blow_outs_games = (score_diff >= 17).sum()

"""How many games were competitive"""
amount_competitive_games = score_diff.between(9, 16).sum()

"""How many games were close"""
amount_close_games = (score_diff.between(1, 8)).sum()

"""How many home teams won"""
amount_home_wins = (game_data['score_home'] > game_data['score_away']).sum()

"""How many away teams won"""
amount_away_wins = (game_data['score_away'] > game_data['score_home']).sum()

"""What are the descriptive values for away points"""
descriptive_away_points = utils.get_basic_stats(game_data, 'score_away')

"""What are the descriptive values for home points"""
descriptive_home_points = utils.get_basic_stats(game_data, 'score_home')

"""What are the descriptive values for total points in a game"""
game_data['total_points'] = game_data['score_home'] + game_data['score_away']
descriptive_total_points = utils.get_basic_stats(game_data, 'total_points')


# print(f"amount_blow_outs_games: {amount_blow_outs_games}")
# print(f"amount_competitive_games: {amount_competitive_games}")
# print(f"amount_close_games: {amount_close_games}")

print(f"amount_home_wins: {amount_home_wins}")
print(f"amount_away_wins: {amount_away_wins}")

# print(f"descriptive_away_points : {descriptive_away_points }")
# print(f"descriptive_home_points : {descriptive_home_points }")
# print(f"descriptive_total_points: {descriptive_total_points}")
