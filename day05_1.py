#출력
#print
#print(123123)
#print('asdasd')

#변수와 자료형

변수 = '저장공간'
정수형 = 123
실수형 = 3.14

변수 = '문자열형'

print(정수형)
print(실수형)
print(변수)
print('내가 저장한 값:',변수,',',실수형)
print('내가 저장한 값:{},{}'.format(변수,실수형))
print(f'내가 저장한 값:{변수},{실수형}')

#리스트,튜플,세트,딕셔너리 (하나의 변수에 여러개의 값을 저장하려고)

lst= [1,2,3,4,'hello',5,6]
tup= (1,2,3, 'hello',4,5,6) #수정 불가
sst= {1,2,3, 'hello',4,5,6}     #중복 불가
dic= {'A':'에이','b':'비'}   #키 지정

lst.append('맨 뒤에 추가')
print(lst)
lst.pop()
print(lst)

for item in lst:
    print(item,end='')


dic['추가 할 키워드']= '추가할 값' #추가
dic[1]= '일' #수정(기존 키워드)
print(dic)

print(lst[0])  #0~
print(dic["a"]) #지정한 키워드

#딕셔너리 전체 표현
for i in dic:
    print(dic[i],end=' ')
    # print(dic.get(i),end=' ') #get을 사용해도 됨
 
# print()
 #입력  (변수가 필요)
변수 = input('입력할 문자열을 입력하세요>>>')
정수형 = int(input('입력할 정수를 알려주세요>>>'))
print('내가 입력한 문자열:',변수,'\n내가 입력한 정수형:',정수형)

#조건문/반복문

if  정수형 <10:
    print('10보다 작네요')
elif 정수형 < 100:
    print('100보다 작네요')
else:
    print('100이상')

for i in range(5):
    print('5번 반복',i)

for i in lst:
    if i == 'hello':
        print('hello 찾음')
        break #반복문을 즉시 종료



