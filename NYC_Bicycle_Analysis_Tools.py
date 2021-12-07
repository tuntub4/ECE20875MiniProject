import csv
import re

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

        for n in range(0,len(col)):
            col[n] = (col[n] - mean[i]) / std[i]
        X.append(col)
    
    X = np.array(X).transpose()

    return X, mean, std
