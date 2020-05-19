from os import path, stat
import time
import requests

import pandas as pd

def is_too_old(filepath):
    file_age = time.time() - path.getmtime(filepath)

    seconds = file_age
    minutes = int(seconds) / 60
    hours = minutes / 60
    days = hours / 24
    
    return days > 1

def file_not_found(filepath):
    return not path.isfile(filepath)

def get_red_wine_data():
    filename = 'red_wine_quality.csv'
    
    if file_not_found(filename):
        red = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
        red.to_csv(filename)
        
    elif is_too_old(filename):
        red = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
        red.to_csv(filename)
        
    return pd.read_csv(filename, index_col='Unnamed: 0')

def get_white_wine_data():
    filename = 'white_wine_quality.csv'
    
    if file_not_found(filename):
        red = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')
        red.to_csv(filename)
    
    elif is_too_old(filename):
        red = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')
        red.to_csv(filename)
        
    return pd.read_csv(filename, index_col='Unnamed: 0')

def get_wine_names_file():
    filename = 'winequality.names'
    
    if file_not_found(filename):
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names'
        myfile = requests.get(url)
        open('./winequality.names', 'wb').write(myfile.content)
    
    elif is_too_old(filename):
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names'
        myfile = requests.get(url)
        open('./winequality.names', 'wb').write(myfile.content)