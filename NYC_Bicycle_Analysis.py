from NYC_Bicycle_Analysis_Tools import *
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import numpy as np

def select_bridges(bridge_counts, totals, bridge_names):
    #Most accuarate regression will have greatest r^2 value for the three chosen bridges
    

    r_squared = []
    for i in range(len(bridge_counts)):
        temp_bridges = bridge_counts[:i] + bridge_counts[i+1:]
        X = np.array(temp_bridges).T
        y = totals

        [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)
        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        score = model.score(X_test, y_test)
        r_squared.append(score)

    bridge_names.pop(r_squared.index(max(r_squared)))
    selected_bridges = bridge_names
    return r_squared, selected_bridges

def linreg_traffic_and_weather(high_temps, low_temps, precipitation, totals):
    X = np.array([high_temps, low_temps, precipitation]).T
    y = totals
    [X_train, X_test, y_train, y_test] = train_test_split(X, y, test_size=0.25, random_state=101)
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    X_test = normalize_test(X_test, trn_mean, trn_std)

    model = train_model(X_train, y_train, 1)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    score = model.score(X_test, y_test)
    return score

def predict_raining(precipitation, totals, min_precip):
    X = np.array([totals]).T
    y = precipitation

    is_raining = [0 if precip <= min_precip else 1 for precip in y]

    [X_train, X_test, y_train, y_test] = train_test_split(X, is_raining, test_size=0.25, random_state=0)

    model = GaussianNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    score = model.score(X_test, y_test)
    con_mat = confusion_matrix(y_test, y_pred)
    return score, con_mat

def display_results():
    data = get_data("NYC_Bicycle_Counts_2016_Corrected.csv")
    bridge_counts = get_bridge_counts(data)
    totals = get_totals(data)
    bridge_names = ["Brooklyn", "Manhattan", "Williamsburg", "Queensboro"]

    #Problem 1
    bridge_scores, selected_bridges = select_bridges(bridge_counts, totals, bridge_names)
    print("When a linear regression was performed on each 3 bridge combination out of the 4 bridges compared to total traffic, the following results were yielded:")
    for i in range(0, len(bridge_names)+1):
        temp_bridges = ["Brooklyn", "Manhattan", "Williamsburg", "Queensboro"]
        temp_bridges.pop(i)
        print("\nUsing the following bridges:")
        for bridge in temp_bridges:
            print(bridge)
        print("The r^2 value was calculated to be: ", bridge_scores[i])
    
    print("\nThe combination with the greatest r^2 value of", max(bridge_scores), "is:")
    for bridge in selected_bridges:
        print(bridge)

    #Problem 2
    high_temps = get_high_temps(data)
    low_temps = get_low_temps(data)
    precipitation = get_precipitation(data)

    coef_corr_helmets = linreg_traffic_and_weather(high_temps, low_temps, precipitation, totals)
    print("\nWhen a linear regression was performed comparing the weather conditions of high temperatures, low temperatures, and precipitation to total traffic, the following results were yielded:")
    print("The cofficient of correlation was calculated to be:", coef_corr_helmets)
    coef_low = linreg_onestat(low_temps, totals)
    coef_high = linreg_onestat(high_temps, totals)
    coef_prec = linreg_onestat(precipitation, totals)
    coef_highlow = linreg_twostat(low_temps, high_temps, totals)
    coef_lowprec = linreg_twostat(low_temps, precipitation, totals)
    coef_highprec = linreg_twostat(high_temps, precipitation, totals)
    print("The cofficient of correlation for low temp was calculated to be:", coef_low)
    print("The cofficient of correlation for high temp was calculated to be:", coef_high)
    print("The cofficient of correlation for prec was calculated to be:", coef_prec)
    print("The cofficient of correlation for high low was calculated to be:", coef_highlow)
    print("The cofficient of correlation for low prec was calculated to be:", coef_lowprec)
    print("The cofficient of correlation for high prec was calculated to be:", coef_highprec)

    #Problem 3
    accuracy = []
    con_mats = []
    precip_range = np.array(range(0,25,1)) / 100
    for min_precip in precip_range:
        coef_raining, con_mat = predict_raining(precipitation, totals, min_precip)
        con_mats.append(con_mat)
        accuracy.append(coef_raining)
    print("The Gaussian Naive Bayes model comparing total traffic to precipitation was about to correctly predict if there was rain", accuracy[0]*100, "% of the time")
    print("However, some days with very low precipitation may be treated as negligable")
    print("The Naive Bayes model was applied with raining defined as a minimum precipitation ranging from 0-0.25\" in 0.01\" increments")
    print(con_mats[0])
    plt.plot(precip_range, accuracy, "o")
    plt.xlabel("Minimum Precipitation (inches)")
    plt.ylabel("Naive Bayes Prediction Accuracy")
    plt.title("Naive Bayes Model Accuracy as a function of Defined Minimum Precipitation")
    plt.show()
    


display_results()


