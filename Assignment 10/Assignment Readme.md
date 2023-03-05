# Time Series & Regression Analysis with ARAM, ARIAM, and GARCH Models


## This Readme file has the Following Sections:
1. Time Series Analysis.
2. Regression Analysis.



## Time Series Analysis:

Overall: 1990 to 2020:
Overall, from the graph, the exhange rate price fluctures around it's average, the trend is relatively stable. <br> In the short-term,  there is no seasonal patteren for each year. <br> For the long-term, the exchange rate price cycles from low to low every six to eight years. 
![](pics/1.png)

Recent 2015 to 2020: 
There is no clear patterns for this period. <br> But it could be noticeable that the exchange rate prices were close for the beginning and the end of each year. <br> And overall, for this five year period, there was a slighly decreasing trend.
![](pics/2.png)

## ARAM:
The ARAM model sugguests the CAD/JAP exchange price would flucture over next 5 days.
![](pics/3.png)

## ARIAM:
The model forecasts CAD/JPY exchange rate price would decrease in the next five days. In the other words, Japanese Yen would appreciate agaisnt CAD.
![](pics/4.png)

## GARCH:
The model forecast the volatility will increase over next five days.
<br>
![](pics/5.png)

## Conclusion:
* The result from ARIMA model implies Yen would appreciate agaisnt CAD, so I would consider to buy yen now.

* However, overall, the models need to be modified and tested.
    <br>ARARM model, lag two is insginificant, the model is not in a good fit yet, itmight need to consider a PACF ACF to re-investigate which lags to be included in the model.
    <br>ARIMA model is NOT in a good fit, as ALL of its parameters are statistically insignificant from zero (P-value > 0.05)
    <br>Although Our p-values for GARCH and volatility forecasts tend to be much lower than our ARMA/ARIMA return and price forecasts.



## Regression Analysis:
Comparing test (actual) vs. prediction:
***The historical data has been splited in to train (1990 to 2017) and test (2018 to 2020)***
![](pics/6.png)

Comparing RMSE:
<br> Comparing the two RMSE's, the RMSE from the out-of-sample data is 0.645, whereas it is 0.842 from the in-sample data model.
<br> The out-of-sample performs better, as its RMSE is lower than the in-sample RMSE. RMSE is typically lower for training data, but is higher in this case. 
