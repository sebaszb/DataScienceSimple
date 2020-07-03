# Spark related machinery
import pyspark
import pyspark.sql.functions as F
from pyspark import SparkConf
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql import HiveContext
from pyspark.sql.functions import concat_ws

spark = pyspark.sql.SparkSession.builder.enableHiveSupport().getOrCreate()


def create_players_table():
    '''
    This function creates a spark table with the following
    columns:
    * Name
    * Age
    * Game
    * Player_id
    '''
    
    player_info = [("Nicolas", 25, "Doom", 1),
               ("Camila",  23, "Diablo", 2),
               ("Gabriel", 20, "Wolfenstein", 3),
               ("Mateo",   23, "Zelda BOTW", 4),
               ("Luna",    21, "Mario", 5),
               ("Lily",    25, "Counter Strike", 6),
               ("Sofia",   26, "Max Payne", 7),
               ("Leo",     28, "Fifa 20", 8),
               ("Thomas",  22, "Speed", 9),
               ("James",   30, "Goldeneye 007", 15),
              ]
    
    players_df = spark.createDataFrame(player_info, ["Name", "Age", "Game", "Player_id"])
    return players_df

def create_new_players_table():
    '''
    This function creates a spark table with the following
    columns:
    * Name
    * Age
    * Game
    * Player_id
    '''
    
    new_players_info = [("Mia", 22, "Mario", 10),
                        ("David",  28, "Diablo", 11),
                        ("Dylan", 21, "Doom", 12)
                       ]
    
    new_players_df = spark.createDataFrame(new_players_info, ["Name", "Age", "Game", "Player_id"])
    return new_players_df

def create_ranking_table():
    '''
    This function creates a spark table with the following
    columns:
    * Player_id
    * Ranking
    '''
    
    ranking_info = [(1, 1),
                    (2, 1),
                    (3, 4),
                    (4, 9),
                    (5, 2),
                    (6, 3),
                    (7, 99),
                    (8, 22),
                    (9, 12), 
                    (10, 440),
                    (11, 21)]
    
    ranking_table = spark.createDataFrame(ranking_info, ["Player_id", "Ranking"])
    return ranking_table
