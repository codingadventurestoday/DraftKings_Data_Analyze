import utils


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

"""How many games were blow outs"""

"""How many games were competitive"""

"""How many games were close"""

"""How many home teams won"""

"""How many away teams won"""

"""What are the descriptive values for points"""

"""What are the descriptive values for away points"""

"""What are the descriptive values for home points"""

"""What are the descriptive values for total points in a game"""


