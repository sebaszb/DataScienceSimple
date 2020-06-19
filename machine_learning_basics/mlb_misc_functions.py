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
