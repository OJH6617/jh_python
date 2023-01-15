#세트 set ={}
#잠깐! 변수이름을 자료형으로 쓰면 안된다


#set>>>> 중복이 안됨
#중복된 값을 추가하려 하면 무시를 해버림
s =set({})
s2={'a','c','e'}
#추가 add
s.add('a')
s.add('b')
s.add('c')
s.add('d')

print(s)
print(s2)


#빼려면, remove사용
s.remove('d')
print(s)
print(s2)

#set는 (중복X)
#수학적으로 사용될 수 있다.
#교집합(set중 일치하는 값만 가지고 올 수 있다.)
s_kyo = s & s2
print(s_kyo) 
#합집합
s_sum=s-s2
print(s_sum)

#차집합 (s에만 있고 s2에는 없는 것)
s_sub= s-s2