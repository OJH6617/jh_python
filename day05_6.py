#외부함수를 사용하는 법 : import
#다른사람이 만든 함수를 사용하는 법임

#import  모듈명
#import 모듈명 as 별명
#from 모듈명 import 함수명


import matplotlib.pyplot as plt   #모듈명을 plt로 하겠다
from matplotlib import font_manager, rc    # 모듈중에 front_manager와 rc 부분만 가져옴

font = font_manager.FontProperties(fname='gulim.ttc').get_name()
rc('font', family=font)

lst =[10,20,12,31,41,90,66,11,44,88]
plt.title('분포도')                      #제목써줘
plt.xlabel('점수')                    #x축제목
plt.ylabel('갯수')          #y축 제목
plt.hist(lst)        #막대그래프 그려줘
plt.show()               # 보여줘
