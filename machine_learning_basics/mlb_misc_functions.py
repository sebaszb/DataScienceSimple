from random import random
import numpy as np

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
