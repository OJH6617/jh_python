# 문자열 = 'hello world, my name is pyhton'
# 정수 = 314
# 실수= 3.14

# # for i in 문자열:
# #     print(i,end='     ')

# i=0
# while i < len(문자열):
#     print(문자열[i], end='  ')
#     i+=1


#문제=문자열에서 알파벳 o의 갯수를 알려주세요
문자열 = ['h','e','l','l','o', 'w','o','r','l','d', 'm','y', 'n','a','m','e', 'i','s', 'p','y','h','t','o','n']
for i in (문자열):
    if i=='o':
        print(i)
    

#자료형중에 str int float list tuple dict set
#list
#지하철 3칸,  각각 칸에 10, 15, 12
subway1 = 10
subway2 = 15
subway3 = 12
print(' ')
#원래는 이렇게 해야하지만 지하철칸이 너무 많으면 불가능함.
#그래서 리스트라는게 있음 한번에 저장하고 한번에 출력
리스트=[10,15,12]
for i in 리스트:
    print(i,'명')


#문제 1~12월을 출력하되 입력받은 월은  skip
# 월=int(input('월을 입력하세요'))
# for i in range(12):
#     if i==(월-1):
#         continue
#     print((i+1),'월')
     







# #문제 1월 12월을 출력하되 입력받은 월 부터는 출력x
# 월=int(input('월을 입력하세요'))
# for i in range(12):
#     if i>=(월-1): 
#         continue
#     print((i+1),'월')
     