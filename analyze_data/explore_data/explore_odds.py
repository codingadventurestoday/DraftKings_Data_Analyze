import numpy as np
import pandas as pd

from get_information.data_mysql import get_data
from analyze_data.explore_data import utils

"""run file from root dir: python3 -m analyze_data.explore_data.explore_odds.py"""

"""
oddsID SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
gameID SMALLINT UNSIGNED,
date_gathered DATE,
over_under DECIMAL(4,1),
over_odds SMALLINT,
under_odds SMALLINT,
home_spread DECIMAL(3,1),
away_spread DECIMAL(3,1),
home_spread_odds SMALLINT,
away_spread_odds SMALLINT,
home_moneyline SMALLINT,
away_moneyline SMALLINT
"""

odds_game_query = f"SELECT odds.* FROM odds JOIN games ON odds.gameID = games.gameID WHERE games.game_date <= NOW();"

odds_df = get_data(odds_game_query)

unique_game_home_spread = odds_df.groupby('gameID')['home_spread'].mean()

pick_em_games = (unique_game_home_spread == 0 ).sum()

"""How many home games were expected to be blow outs"""
projected_home_blow_outs = (unique_game_home_spread < -16).sum()

"""How many home games were expected to be competitive"""
projected_home_competitive = (unique_game_home_spread.between(-16, -8,inclusive='left')).sum()

"""How many home games were expected to be close"""
projected_home_close = (unique_game_home_spread.between(-8, 0.0,inclusive='left')).sum()


"""How many away games were expected to be blow outs"""
projected_away_blow_outs = (unique_game_home_spread > 16).sum()

"""How many away games were expected to be competitive"""
projected_away_competitive = (unique_game_home_spread.between(8, 16,inclusive='right')).sum()

"""How many away games were expected to be close"""
projected_away_close = (unique_game_home_spread.between(0.0,8,inclusive='right')).sum()

"""How many games were expected to be blow outs"""
total_projected_blow_outs = projected_away_blow_outs + projected_home_blow_outs

"""How many games were expected to be competitive"""
total_projected_competitive = projected_away_competitive + projected_home_competitive

"""How many games were expected to be close"""
total_projected_close = projected_away_close + projected_home_close + pick_em_games

"""What are the descriptive values for games"""

"""What are the descriptive values for away games"""

"""What are the descriptive values for home games"""


"""What are the descriptive values for over_unders"""
over_under_descriptive = utils.get_basic_stats(odds_df, 'over_under')

"""What are the descriptive values for over odds"""
over_odds_descriptive = utils.get_basic_stats(odds_df, 'over_odds')

"""What are the descriptive values for under odds"""
under_odds_descriptive = utils.get_basic_stats(odds_df, 'under_odds')

"""What are the descriptive values for home_spreads odds"""
home_spread_descriptive = utils.get_basic_stats(odds_df, 'home_spread')

"""What are the descriptive values for away_spreads odds"""
away_spread_descriptive = utils.get_basic_stats(odds_df, 'away_spread')

"""What are the descriptive values for home moneylines"""
home_moneyline_descriptive = utils.get_basic_stats(odds_df, 'home_moneyline')

"""What are the descriptive values for away moneylines"""
away_moneyline_descriptive = utils.get_basic_stats(odds_df, 'away_moneyline')

"""are home or away teams expected to win more often"""
conditions = [
    unique_game_home_spread > 0,
    unique_game_home_spread < 0
]

choices = ['Home', 'Away']

favorites = np.select(conditions, choices, default='Pick Em')
fav_counts = pd.Series(favorites).value_counts()
fav_percentages = pd.Series(favorites).value_counts(normalize=True) * 100

# print(f"projected_home_blow_outs: {projected_home_blow_outs}")
# print(f"projected_home_competitive: {projected_home_competitive}")
# print(f"projected_home_close: {projected_home_close}\n")

# print(f"projected_away_blow_outs: {projected_away_blow_outs}")
# print(f"projected_away_competitive: {projected_away_competitive}")
# print(f"projected_away_close: {projected_away_close}\n")

print(f"total_projected_blow_outs: {total_projected_blow_outs}")
print(f"total_projected_competitive: {total_projected_competitive}")
print(f"total_projected_close: {total_projected_close}\n")

# print(f"over_under_odds_descriptive: {over_under_descriptive}")
# print(f"over_odds_descriptive: {over_odds_descriptive}")
# print(f"under_odds_descriptive: {under_odds_descriptive}\n")

# print(f"home_spread_descriptive: {home_spread_descriptive}")
# print(f"away_spread_descriptive: {away_spread_descriptive}")

# print(f"home_moneyline_descriptive: {home_moneyline_descriptive}")
# print(f"away_moneyline_descriptive: {away_moneyline_descriptive}\n")

print(f"fav_counts: {fav_counts}")
# print(f"fav_percentages: {fav_percentages}")

