#제어문 중첩
#조건문 안에서 조건문
# if True:
#     print('조건문1 실행')
#     if False:
#         print('조건문2 실행')
#         print('조건문2 종료')
#     print('조건문2 종료')
# #조건문 안에서 반복문
# if True:
#     print('조건문1 실행')
#     for i in range(3):
#         print('반복문1을',(i+1),'번째 실행')
#     print('조건문1 종료')
    
#반복문 안에서 조건문
# for i in range(3):
#     print('반복문1을',(i+1),'번째 실행')
#     if True:
#         print('조건문1 실행')
#         print('조건문1 종료')
#     print('반복문1을',(i+1),'번째 종료')


#반복문 안에서 반복문 (2차원 행렬)
# for i in range(3):
#     print('1A',(i+1))
#     for z in range(3):
#         print('2B',(z+1))
#     print('')

for i in range(1,11):
    for j in range(1,11):
        print(j,end=' ')
    print()


