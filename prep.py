import pandas as pd

from sklearn.model_selection import train_test_split

import acquire

def prep_white_wine_data():
    white = acquire.get_white_wine_data()
    white.columns = white.columns.str.replace(' ', '_')
    train, test = train_test_split(white, train_size=.85, random_state=13)
    train, val = train_test_split(train, train_size=.82, random_state=13)
    
    return train, val, test

def prep_red_wine_data():
    red = acquire.get_red_wine_data()
    red.columns = red.columns.str.replace(' ', '_')
    train, test = train_test_split(red, train_size=.85, random_state=13)
    train, val = train_test_split(train, train_size=.82, random_state=13)
    
    return train, val, test