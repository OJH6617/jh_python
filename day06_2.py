#내장 함수: 파이썬 내장함수 (파이썬 언어에서 제공하는 기능)

#eval() : 문자열 형태의 연산식을 정수로 계산
result=eval('5+5') 
print('5+5')
print(result)

#format(): 문자열로 변환
result=format(10000)
#type(): 변수의 자료형태를 알려줌
print(type(result))

#str(): 문자열로 변환 >>>주로 이걸 많이 씀
print(str(3.14))    #'3.14'
#int()
#float()

#list(), tuple() set() dict() : 형변환

lst=[1,2,3]
print(lst)
print(tuple(lst))

result = format(100000000000000, '_') #1000단위로 끊어서 표시해준다
print(result)


#max()
result = max(lst)
print(result)
#min()
result = min(lst)
print(result)
#sum(): 리스트 전체 합계
result = sum(lst)
print(result)
#len(): 리스트에 저장된 갯수
result = len(lst)

#abs() : 절댓값
result = abs(-4)
print(result)
#pow():  제곱승
#10^3 (10의3제곱을 하고싶다)
print(pow(10,3))

#divmod(): tuple(몫,나머지)
result = divmod(10,3)
print(result)

#round(): 반올림
#3.141592를 둘째자리까지 반올림
result=round(3.141592, 2)
print(result)
result=round(3.555555)
print(result)

#enumerate(): 반복문이랑 같이 사용됨, 리스트를 여러개의 튜플로
#lst=[1,2,3] >> (0,1), (1,2), (2,3)
#hello = ['h','e','l','l','o'] >> (0,'h')(1,'e')(2,'l')(3,'l')(4,'o')
hello = ['h','e','l','l','o']
for item in enumerate(hello):
    print(item)

#문제1>> pow함수를 직접 한번 만들어보자
def 포우(num1,num2):
    result = 1
    for i in range(num2):
        result=result*num1
    return result
print(포우(10,3))

  

#range(n) :0부터n까지 반복한다.
#range(n,m): n~m-1까지 반복(m-n번 반복)
#range(n,m,k):n~m-1까지 반복을 하되 간격을 k만큼 뛰면서(기본값1)
for i in range(3):
    print('3번 반복',i) #i==0,1,2

for i in range(1,3):
    print('3-1번 반복',i) #i==1,2

for i in range(1,10,2):
    print(i)   # i==1,3,5,7,9

#sorted() :리스트를 오름차순으로 정렬해줌
lst=[3,4,1,2,7,6,9]
lst2=sorted(lst)
print(lst2)

# 내림차순정렬
lst3=sorted(lst,reverse=True)
print(lst3)
