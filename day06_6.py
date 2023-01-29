import sklearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
원본데이터 = pd.read_csv('kyobo.csv',encoding='cp949')
print(원본데이터)
x=원본데이터.iloc[:,:-1].values
y=원본데이터.iloc[:,-1].values
print(x)
print(y)
선형기계학습=LinearRegression()


선형기계학습.fit(x,y)
y_pred =선형기계학습.predict(x)
print('예측한 y값:\n', y_pred)




plt.scatter(x,y,color='navy') 
plt.plot(x,y_pred,color='brown') 
plt.title('')                  
plt.xlabel('number of visitors')            
plt.ylabel('sales volume')    
plt.show()

print('ai예측값:',선형기계학습.predict([[300]]))







