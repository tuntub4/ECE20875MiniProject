# ECE20875MiniProject
Dataset Description:

The dataset is organized in a .csv file as chronological daily entries of bicycle traffic and weather across four New York City bridges over a 6 month period. The traffic data includes traffic on each individual bridge as well as the total daily traffic, while the weather data includes the daily high and low temperatures and precipitation.

Analysis Technique Applied:

In order to select the three bridges that could be most accurately used to predict overall traffic, we performed a linear regression comparing traffic on each three bridge combination to total traffic. Each regression yields a r2 value ranging from zero to one which describes how closely the features correlate to the total traffic. By selecting the regression with the greatest r2 value, we can suggest that the bridges used in this regression most accurately predict the total traffic, and thus the monitoring sensors should be placed on these bridges.

Similar to the regression used to analyze sensor placement on the bridges, a regression can be performed comparing various weather factors to total traffic in order to determine if there is a relationship between weather conditions and bicycle traffic. We used the data for high temperature, low temperature, and precipitation for our features. To cover a complete scope of the relationships, we decided to perform a regression comparing each feature individually as well as every combination of features against total traffic. Each regression will yield an r2 value which can be used to assess how closely the feature(s) can be used to determine total traffic. If any r2 values are close to one, those features are typically reliable indicators of total traffic and the weather forecast for these values can be used to predict the number of bicyclists. 

In order to determine if it was possible to predict if it was raining based on total traffic, we decided to use a Gaussian Naive Bayes model since the condition of rainfall is being treated as a discrete value. This also assumes that total traffic follows a normal distribution. Using this strategy will yield an accuracy score as to how often the model is able to predict if it is raining. Another factor we want to consider is that certain levels of rain could be considered negligible as they would either not be noticable, only happen during certain hours of the day, or would not affect the ability to use a bicycle. Accounting for these negligible values could increase the model accuracy, so we performed the execution of the model on a range of values that would be used as the minimum precipitation level to define rainfall.

Analysis Results:

1. 

Bridge Combination
Manhattan, Williamsburg,
Queensboro
Brooklyn,
Williamsburg,
Queensboro
Brooklyn,
Manhattan,
Queensboro
Brooklyn,
Manhattan,
Williamsburg
r2
0.99147
0.97700
0.99435
0.99741

Figure 1.0

After performing a linear regression on each three bridge combination we calculated the r2 values as shown in figure 1.0. We found that the combination of the Brooklyn Bridge, Manhattan Bridge, and Williamsburg Bridge yielded the greatest r2 value and thus had the strongest correlation to total traffic. Therefore, the monitoring sensors should be installed on these three bridges.

2.

Feature Combination
r2
Low Temperature
0.20375
High Temperature
0.40116
Precipitation
0.21169
Low Temperature, High Temperature
0.47348
Low Temperature, Precipitation
0.45230
High Temperature, Precipitation
0.59028
Low Temperature, High Temperature,
Precipitation
0.61749

Figure 2.0

Since some of the r2 values for the weather data shown in figure 2.0 had decent correlation (r2 close to 1), the next day’s weather pattern is a somewhat accurate predictor of the number of cyclists for that day. The best predictor is found when comparing the low and high temperatures and the precipitation, yielding an r2 value of .61749, which means that only around 62% of the variation in the traffic is explained by the weather data (low and high temperature and precipitation). Overall, since the weather data explains around 62% of the variation in bicycle traffic, it is a moderate predictor, but should not be used as the sole factor when trying to predict the number of cyclists. Since this relationship is not strong, it would be wise to include other indicators to strengthen the prediction. 

3.

By using the Naive Bayes model, we were able to determine that bicycle traffic can correctly determine if it is raining 77.78% of the time, which total traffic is a fairly accurate indicator for rainfall. However, if there was very little rainfall, only 0.03” for example, this would likely not affect bicycle traffic significantly. To analyze this possibility, we conducted the model with a minimum precipitation to be defined as rainfall ranging from 0-0.25” in 0.01” increments. As the threshold increases, it is likely that the model will increase in accuracy when negligible values are not counted as rainfall, however, it is ultimately the decision of city administration as to what levels of rainfall should be treated as significant. We plotted the accuracy of the model against the minimum defined value as shown:

Figure 3.0
Figure 3.0 shows that the model becomes more accurate to a level of over 95% as the threshold defining rainfall increases. If a safe threshold in this range could be determined, the model can be used even more reliably than if any rainfall was counted as significant. In either case, the model concludes that total traffic can be used to predict if it is raining at least 77.78% of the time, and a potentially greater percentage of the time with a selected threshold.
