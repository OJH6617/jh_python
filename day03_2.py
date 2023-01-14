#반복문(while, for)
#for를 사용해서  hello 3번하기

# for 임시변수 in range(3):
#     print('hello')

# #여기서 임시변수의 역할 : while에서 i 를 값으로 사용 ..>임시변수
# i=0
# while i<3:
#     print(i,'번째 hello')
#     i +=1

# for j in range(3):
#     print(j,'번째 hello')


# #for를 1부터 시작하려고 하면 어떻게 하나

# for i in range(1,4):
#     print(i,'번째 헬로')
# #range(3) ....>range(0,3)
# #range(1,4)....>1부터 4'전'까지!! 중요


# #1월 부터 12월을 출력해보세요

# for i in range(1,13):
#     print(i,'월')
#     i+=1

# for i in range(0,101,7):
#     print(i)

# #짝수만 출력하기
# for i in range(0,11,2):
#     print(i)


#문제
5
4
3
2
1
#문제2
#양의정수 한개를 입력받아서
#1부터 입력한 숫자까지 합께를 알려주는 프로그램

# ex)10 --> 55

#문제1

for z in range(5,0,-1):
    print(z)

num = 5
for i in range(5):
    print(num)
    num-=1
  



#문제2
z=0
양의정수 = int(input('양의정수 를 입력하세요'))
for a in range(1,양의정수+1):
    z+=a
    print('합은',z,'입니다')

#문제3
num1=1
num2=2
backup=0
backup=num1
num1=num2
num2=backup
print(num1,num2)
        
        
        
    
