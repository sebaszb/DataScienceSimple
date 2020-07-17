import pandas as pd
import numpy as np

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
