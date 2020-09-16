# Spark related machinery
import pyspark
import pyspark.sql.functions as F
from pyspark import SparkConf
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql import HiveContext
from pyspark.sql.functions import concat_ws

spark = pyspark.sql.SparkSession.builder.enableHiveSupport().getOrCreate()

import pandas as pd
import numpy as np
from random import randint


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

def create_sp_table1():
    '''
    This function creates a spark table with 4 columns:
    * student_id: Unique row identifier
    * exam_1: Random number between 0 and 10
    * exam_2: Random number between 0 and 10
    * exam_3: Random number between 0 and 10

    The table has 1000 rows.

    '''
    #Create table
    pd_df = pd.DataFrame()
    
    #create columns
    pd_df["student_id"] = [i for i in range(1, 1001)]
    pd_df["exam_1"] = [np.random.randint(0, 11) for i in range(1, 1001)]
    pd_df["exam_2"] = [np.random.randint(0, 11) for i in range(1, 1001)]
    pd_df["exam_3"] = [np.random.randint(0, 11) for i in range(1, 1001)]
    
    df = spark.createDataFrame(pd_df)
    return df

def create_sp_table2():
    '''
    This function creates a table with 6 columns:
    * participant_id: Unique row identifier
    * name: Name of the player
    * last_name: last name of the player
    * age: Age of the player
    * score_game_1: Score obtained in game 1
    * score_game_1: score obtained in game 2
    '''
    
    #Create table
    df = pd.DataFrame()
    
    #Add row id
    df["participant_id"] = [i for i in range(1, 11)]
    
    #Add name
    df["name"] = ["Sophia",
                  "Liam",
                  "Olivia",
                  "Jackson",
                  "Ava",
                  "Oliver",
                  "Lucas",
                  "Mia",
                  "Aria",
                  "Amelia"
                 ]
    
    #Add last name
    df["last_name"] = ["Lara",
                       "Smith",
                       "Wilson",
                       "Garcia",
                       "Moore",
                       "Leon",
                       "Brown",
                       "Lee",
                       "Robinson",
                       "Walker"
                      ]
    #Add age
    df["age"] = [27,
                 23,
                 25,
                 24,
                 26,
                 30,
                 24,
                 31,
                 28,
                 29
                ]
    
    df["score_game_1"] = [89,
                         50,
                         78,
                         98,
                         100,
                         65,
                         78,
                         85,
                         80,
                         93
                        ]
    
    
    df["score_game_2"] = [84,
                          60,
                          70,
                          90,
                          89,
                          70,
                          75,
                          79,
                          89,
                          99
                         ]
    
    sp_df = spark.createDataFrame(df)
    return sp_df

def create_sp_table3():
    #Create table
    df_pd = pd.DataFrame()
    
    #Id column (not unique)
    df_pd["id"] = [randint(1, 5) for i in range(0, 20)]
    
    #Team
    df_pd["team"] = [randint(1, 3) for i in range(0, 20)]
    
    #Score
    df_pd["score"] = [randint(0, 100) for i in range(0, 20)]
    
    df = spark.createDataFrame(df_pd)
    return df