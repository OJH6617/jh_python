#pip install scikit.learn
# 머신러닝 모듈
import sklearn
#그래프 모듊
import matplotlib.pyplot as plt
#수학/과학 계산 모듈
import numpy as np
#다자원 데이터 모듈
import pandas as pd
from sklearn.linear_model import LinearRegression

print(sklearn.__version__)

...
#머신러닝:데이터(정제된)>>기계학습>>에측결과>>머신러닝별 비교 후 선정
...
#데이터를 가져온다 csv
원본데이터 = pd.read_csv('smaple.csv',encoding='cp949')
print(원본데이터.head(7)) #상위 7개만 보겠다//

x=원본데이터.iloc[:,:-1].values
y=원본데이터.iloc[:,-1].values
print(x)
print(y)

선형기계학습=LinearRegression()
선형기계학습.fit(x,y) #원인은 이거고 결과는 이거니까 학습을 해.
#predict 학습한 내용을 바탕으로 예측을 해
y_pred =선형기계학습.predict(x)
print('예측한 y값:\n', y_pred)

print('ai예측값:',선형기계학습.predict([[4.5]]))

#점찍기
plt.scatter(x,y,color='green') #원본데이터는 점으로 그려줘
plt.plot(x,y_pred,color='red') #에측데이터는 선으로 그려줘
plt.title('')                  #제목 정해줘
plt.xlabel('hours')            #x축 제목 정해줘
plt.ylabel('corrsion rate')    #y축 제목 정해줘
plt.show()








