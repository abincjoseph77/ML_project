import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


df = pd.read_csv(r"E:\abin\ABIN\Upscode\pandas\study_data.csv")
print(df.info())


#define veriable
x=df[['study_hours_without_mobile_usage']] #split 80% to x_traing 20% of x_test
y=df[['average_score_percentage']]         #split 80% to y_traing 20% of y_test



#spliting 80% traing and 20% of testing
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=42)


#model creation
model = LinearRegression()
#train model with train data
model.fit(x_train,y_train)


#evaluation  x or study hours = [1,4,3,2]
y_predict = model.predict(x_test)

prediction_df = pd.DataFrame({
    "actual:":y_test.squeeze(),
    "predicted":y_predict.squeeze()
})

print(prediction_df)



#prediction of a student based on this model
n1_x = pd.DataFrame([[3]])  #---> study hour
result = model.predict(n1_x)
print(result)