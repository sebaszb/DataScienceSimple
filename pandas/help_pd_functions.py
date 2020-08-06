import pandas as pd
import numpy as np
from random import randint

def create_pd_table():
    '''
    This function creates a table with 3 columns:
    * student_id: Unique row identifier
    * exam_1: Random number between 0 and 10
    * exam_2: Random number between 0 and 10
    * exam_3: Random number between 0 and 10

    The table has 1000 rows.

    '''
    #Create table
    df = pd.DataFrame()
    
    #create columns
    df["student_id"] = [i for i in range(1, 1001)]
    df["exam_1"] = [np.random.randint(0, 11) for i in range(1, 1001)]
    df["exam_2"] = [np.random.randint(0, 11) for i in range(1, 1001)]
    df["exam_3"] = [np.random.randint(0, 11) for i in range(1, 1001)]
    return df

def create_pd_table2():
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
    return df

def create_pd_table3():
    #Create table
    df = pd.DataFrame()
    
    #Id column (not unique)
    df["id"] = [randint(1, 5) for i in range(0, 20)]
    
    #Team
    df["team"] = [randint(1, 3) for i in range(0, 20)]
    
    #Score
    df["score"] = [randint(0, 100) for i in range(0, 20)]
    return df

def create_pd_table4():
    '''
    This function creates a pandas table with the following columns:
    * car_id: Unique car identifier
    * make: Make of the car
    * year: Year of the car
    * price: current price
    
    '''
    
    #Creates the table
    df = pd.DataFrame()
    
    #Car id column
    df["car_id"] = [i for i in range(1,11)]
    
    #Car make
    df["make"] = ["Mazda",
                  "Toyota",
                  "Ferrari",
                  "Nissan",
                  "Honda",
                  "Kia",
                  "Ford",
                  "Chevrolet",
                  "Tesla",
                  None
                 ]
    
    #Car year
    df["year"] = [2010, 
                  2015,
                  2017,
                  None,
                  2006,
                  2010,
                  2013,
                  2019,
                  2020,
                  2018
                 ]
    
    #Car price
    df["price"] = [5000,
                   7000,
                   None,
                   15000,
                   60000,
                   3000,
                   8000,
                   7500,
                   50000,
                   10000
                  ]
    
    #Car mileage
    df["miles"] = [120000,
                   30000,
                   10000,
                   200000,
                   150000,
                   50000,
                   80000,
                   5000,
                   None,
                   30000
                  ]
    return df