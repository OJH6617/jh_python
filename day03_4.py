#기타 제어믄
#break, continue

#break :  반복문 강제종료
#continue: 반복문이 안끝났어도 위로 올라감(1회성 건너뛰기, 밑에 있는 코드 무시하고 바로 다시 위로 올라감)
for i in range(10):
    print((i+1),'번째 헬로')
    if i >=2:
        break


for i in range(10):
    if i >=3 and i<7:
        continue
    print((i+1),'번째 빠이')

