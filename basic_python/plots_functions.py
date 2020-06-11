from random import random
import numpy as np


def generate_scatter_data_3x():
    '''
    This function generates x - y pairs (100 pairs) on the curve
    y = 3x. A random number is added to each y value
    so the graph wont be a straight line.
    '''
    
    #Declaration of lists
    x = []
    y = []
    
    #Populate the lists
    for i in range(0, 101):
        x.append(i)
        y.append(3 * i)
    
    #generate random numbers
    mu, sigma = 8, 50
    deltas = list(np.random.normal(mu, sigma, 101))
    
    y = list(y[i] + deltas[i] for i in range(0, 101))
    return x, y

def generate_data_x2_2x_1():
    '''
    This function generates x - y pairs (100 pairs) on the curve
    y = x^2 + 2x + 1.
    '''
    
    #Declaration of lists
    x = []
    y = []
    
    #Populate the lists
    for i in range(0, 101):
        x.append(i)
        y.append((i**2) + (2 * i) + 1)
    
    return x, y


def generate_data_75x_p_1():
    '''
    This function generates x - y pairs (100 pairs) on the curve
    y = 2x + 1.
    '''
    
    #Declaration of lists
    x = []
    y = []
    
    #Populate the lists
    for i in range(0, 101):
        x.append(i)
        y.append((75 * i) + 1)
    
    return x, y
