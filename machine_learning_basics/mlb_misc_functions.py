from sklearn.model_selection import train_test_split
from random import random
import numpy as np
import pandas as pd

def generate_dummy_probs_true_y():
    '''
    This funciton returns two lists:
    * true_y: a list containing 0s and 1s (10000 elements)
    * probs: a list containing numbers between 0 and 1 (10000 elements)
    '''
    
    #Number of elements in the list
    N = 10000
    
    #Declaration of the lists
    probs = []
    true_y = []
    
    #populate the probs list with random numbers in the range 0 to 1
    for i in range(0, N):
        probs.append(random())
    
    #Populate the true_y list with
    for val in probs:
        if val > 0.5:
            true_y.append(1)
        if val <= 0.5:
            true_y.append(0)
    
        
    mu, sigma = 0, 0.15
    deltas = list(np.random.normal(mu, sigma, N))
    
    probs = [probs[i] + deltas[i] for i in range(0, N)]
    
    for i in range(0, N):
        if probs[i] > 1.0:
            probs[i] = 0.9999
        if probs[i] < 0:
            probs[i] = 0.001
    return true_y, probs

def create_dummy_modeling_table(size=10000):
    '''
    This function creates a pandas table that resembles 
    a typical modeling table.
    '''
    
    #Create the table
    model_table = pd.DataFrame()
    
    #Create the columns
    model_table["row_id"] = [i for i in range(0, size)]
    model_table["feature_1"] = list(np.random.randint(0, 10, size))
    model_table["feature_2"] = list(np.random.randint(0, 5, size))
    model_table["feature_3"] = list(np.random.randint(0, 5, size))
    model_table["feature_4"] = list(np.random.normal(10, 1, size))
    model_table["target"] = list(np.random.randint(0, 2, size))
    
    return model_table

def create_clf_table_1(size):
    '''
    This function creates a dummy table that resembles the data you would 
    find in a true modeling table where we have a row identifier, 5 features,
    and a target. In this case the target takes the values 1 or 0.
    '''
    data = pd.DataFrame()
    
    data["row_id"] = [i for i in range(0, size)]
    
    data["feature_1"] = list(np.random.randint(-10, 10, size))
    data["feature_2"] = list(np.random.randint(-10, 10, size)) 
    data["feature_3"] = list(np.random.randint(-10, 10, size))
    data["feature_4"] = list(np.random.randint(-10, 10, size))
    data["feature_5"] = list(np.random.randint(-10, 10, size))
    
    data["target"] = data.apply(create_target_1, axis=1)
    return data

def function_grade3(x, y, z, w, k):
    '''
    This function takes in 5 values: x, y, z, w, k and returns:
    x + y + z + w + k +  
    (x*y) + (x*z) + (x*w) + (x*k) + (y*z) + (y*w) + (y*k) + (z*w) + (z*k) + (w*k) + 
    (x**3) + (y**3) + (z**3) + (w**3) + (k**3)
    '''
    linear = x + y + z + w + k
    interactions = (x*y) + (x*z) + (x*w) + (x*k) + (y*z) + (y*w) + (y*k) + (z*w) + (z*k) + (w*k)
    cubes = (x**3) + (y**3) + (z**3) + (w**3) + (k**3)
    value = linear + interactions + cubes
    return  value 

def create_target_1(row):
    '''
    This function creates the target (1 or 0) using the function
    function_grade3
    '''
    x_val = row["feature_1"]
    y_val = row["feature_2"]
    z_val = row["feature_3"]
    w_val = row["feature_4"]
    k_val = row["feature_5"]
    value =  function_grade3(x_val, y_val, z_val, w_val, k_val)
    random_var = np.random.uniform(-300, 300, 1)[0]
    value = value + random_var
    
    value_clf = 0
    
    if value >= 0:
        value_clf = 1
    if value < 0:
        value_clf = 0
    return value_clf

def prep_model_data(df_pd, target, features):
    '''
    This function prepares the data for training and testing (80/20).
    The function takes in:
    * df_pd: Pandas data frame
    * target: list containing one element with the name of the target column
    * features: list containing the name of the features (columns)
    
    The function returns:
    * train_x: List of lists containing numbers. Each sub-list represents the features for each
      observation in the training set.
    * train_y: List containing numbers. Each number represents the target for each
      observation in the training set.
    * test_x: List of lists containing numbers. Each sub-list represents the features for each
      observation in the testing set.
    * test_y: List containing numbers. Each number represents the target for each
      observation in the testing set.
    '''
    
    #split the data into training and testing
    model_train, model_test = train_test_split(df_pd, test_size=0.20, random_state=11)
    
    #Create arrays witht he "x values" (features) and the "y values" (targets) 
    #for the train data
    train_x = model_train[features].values
    train_y = np.ravel(model_train[target].values)
    
    #Create arrays witht he "x values" (features) and the "y values" (targets) 
    #for the test data
    test_x = model_test[features].values
    test_y = np.ravel(model_test[target].values)
    
    return train_x, train_y, test_x, test_y

def create_dummy_scores(num):
    '''
    This functin generates a list containing random
    numbers in the range 0 to 1. the argument "num" 
    determines the number of elements in the list.
    '''
    score = []
    for i in range(0, num):
            score.append(random())
    return score