#리스트 = []
#리스트 : 변수들을 뭉쳐놓은 것
a = 1
b = 2
c = 3
d = 4

abcd=[1,2,3,4] #0번 1번 2번 3번 (방 형태로 구성되어 있다.)

for i in abcd:
    print(i)


# '3'이 저장되어 있는 방번호를 찾아보자!
result=abcd.index(3)
print('3이 저장되어 있는 위치는',result)


#리스트에 저장된 값들 중 하나만 사용하고자 하면
print(abcd[2])

#추가=append
abcd.append(314)

print(abcd)

# 삽입 insert
abcd.insert(2,2222) #나는 2번방에다가 2222를 넣을 것이고 뒤에 것들은 뒤쪽으로 밀어라 2->3 3->4 4->5
print(abcd)



#제거 remove
abcd.remove(2222)
print(abcd) #해당번호를 제거하고 뒤에 남은 것들은 앞으로 밀착시킴

#수정
abcd['들어갈 방 번호']='수정할 내용'

#뒤쪽 부터 뽑기(맨 뒤에 것부터 제거? 라고 보면 됨)

#리무브 쓰면 되지 왜 팝이 있냐 ..> 팝은 뽑아낸걸 저장하는 기능이 있다
#ex
변수 = abcd.pop()
print(변수)

#리스트 비우기 -> clear
abcd.clear()
print(abcd)

#리스트 합치기 extend
abcd2 = [1,2,3,4,5,6,7,8,9,10]
abcd.extend(abcd2)
print(abcd)


#리스트 뒤집기 reverse
abcd.reverse()
print(abcd)

#count

십의갯수= abcd.count(10)
print(십의갯수)
전체갯수 =len(abcd)

#리스트 정렬 sort
abcd.sort()     #기본적으로 낮은 순으로 정렬(오름차순)
print(abcd)

#현재 리스트를 보존하면서 테스트를 하고싶다 >> copy
test_abcd=abcd.copy()
print(test_abcd) #원본을 보존하며 카피본을 만든 것.
