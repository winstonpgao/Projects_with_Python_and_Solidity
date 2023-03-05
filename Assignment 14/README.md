# Testing on - LSTM Stock Predictor
 

### Which model has a lower loss?
The model which fet with the data using only closing prices has **lower** loss of 0.05337 than the model fet with FNG values (0.20438)

### Which model tracks the actual values better over time?
The model which fet with the data using only closing prices tracks **better** as shown in the graph two.

**Graph one fit with FNG Values:**
<br>![Graph one fit with FNG Values](1.png)

**Graph Two fit with Closing Prices:**
<br>![Graph Two fit with Closing Prices](2.png)


### Which window size works best for the model?
Model One fit with FNG Values
Model Two fit with Closing Prices

**Losses:**
<br>**20 Days Window**
<br>Model One 0.18709899485111237
<br>Model Two 0.04786922410130501

**25 Days Window**
<br>Model One 0.1404261738061905
<br>Model Two 0.05402058735489845

**30 Days Window**
<br>Model One 0.16570600867271423
<br>Model Two 0.05828005447983742

<br>By changing the window size, the 25 Days window seems to be the best choice.


**Worth Notice that: Under 25 Days Window**
<br>By changing the number of neurons/units, the result slightly improved.
<br>And when changing the batch size = 5, both models improved as loss decreased much more.
<br>Model One 0.08568271994590759
<br>Model Two 0.028742019087076187
