#import 가 안되는 이유 = 설치가 안된 라이브러리(모듈) 이거나 또는 오타
#외부 모듈 설치 = pip install 모듈형

#pip install python-opencv (일반 파이썬)
#pip install opencv-python (아나콘다 파이썬)


import cv2

# 이미지 = cv2.imread('ing1.PNG') #이미지를 스캔해주ㅡㅓ
# cv2.imshow('title', 이미지) #보여줘
# cv2.waitKey(0)  #보여준 상태로 무한 대기


def cv_ing(path):
    이미지 = cv2.imread('panda.PNG') #이미지를 스캔해주ㅡㅓ
    cv2.imshow('title', 이미지) #보여줘
    cv2.waitKey(0)

cv_ing('panda.PNG')
