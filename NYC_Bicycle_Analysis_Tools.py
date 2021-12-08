import csv
import re
import numpy as np
from sklearn.linear_model import Ridge, Lasso
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

#getter functions to access data
#all string values returned as str and all numerical values returned as floats

def get_data(filename):
    file = open(filename, "r")
    reader = csv.reader(file)
    header = next(reader)
    rows = [row for row in reader]
    file.close()

    return rows

def get_dates(data):
    return [entry[0] for entry in data]

def get_days(data):
    return [entry[1] for entry in data]

def get_high_temps(data):
    return [float(entry[2]) for entry in data]

def get_low_temps(data):
    return [float(entry[3]) for entry in data]

def get_precipitation(data):
    return [float(re.sub("[^0-9\.]", "", entry[4])) if re.sub("[^0-9\.]", "", entry[4]) != '' else 0 for entry in data]

def get_bridge_counts(data):
    #returns biker count arrays on each bridge as an array: [Brooklyn, Manhattan, Williamsburg, Queensboro]
    brooklyn_counts = [float(re.sub("[^0-9\.]", "", entry[5])) for entry in data]
    manhattan_counts = [float(re.sub("[^0-9\.]", "", entry[6])) for entry in data]
    williamsburg_counts = [float(re.sub("[^0-9\.]", "", entry[7])) for entry in data]   
    queensboro_counts = [float(re.sub("[^0-9\.]", "", entry[8])) for entry in data]
    return [brooklyn_counts, manhattan_counts, williamsburg_counts, queensboro_counts]

def get_totals(data):
    return [float(re.sub("[^0-9\.]", "", entry[9])) for entry in data]

def normalize_train(X_train):

    X, mean, std = [], [], []
    for i in range(0,len(X_train[0])):
        col = []
        for j in range(0,len(X_train)):
            col.append(X_train[j][i])
        mean.append(np.mean(col))
        std.append(np.std(col))

        for n in range(0, len(col)):
            col[n] = (col[n] - mean[i]) / std[i]
        X.append(col)
    
    X = np.array(X).transpose()

    return X, mean, std

def normalize_test(X_test, trn_mean, trn_std):

    X = (X_test-trn_mean)/trn_std

    return X

def train_model(X,y,l):

    model = Ridge(alpha=l)
    model.fit(X, y)

    return model

def error(X,y,model):

    y_pred = model.predict(X)
    mse = mean_squared_error(y,y_pred)
    return mse

def linreg_onestat(stat, totals):
    X = np.array([stat]).T
    y = totals
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    X_test = normalize_test(X_test, trn_mean, trn_std)

    model = train_model(X_train, y_train, 1)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    score = model.score(X_test, y_test)
    return score

def linreg_twostat(stat1, stat2, totals):
    X = np.array([stat1,stat2]).T
    y = totals
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    X_test = normalize_test(X_test, trn_mean, trn_std)

    model = train_model(X_train, y_train, 1)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    score = model.score(X_test, y_test)
    return score