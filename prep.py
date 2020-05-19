import pandas as pd

def prep_white_wine_data():
    white = acquire.get_white_wine_data()
    train, test = train_test_split(white, train_size=.85, random_state=13)
    train, val = train_test_split(train, train_size=.82, random_state=13)
    
    return train, val, test

def prep_red_wine_data():
    red = acquire.get_red_wine_data()
    train, test = train_test_split(red, train_size=.85, random_state=13)
    train, val = train_test_split(train, train_size=.82, random_state=13)
    
    return train, val, test