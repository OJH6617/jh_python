# 튜플 tuple 
#tuple = ()
#튜플 : 추가할 수가 없다.

menu = ('돈가스','순두부','김밥')   #리스트랑 다른점 하나 추가 x
print(menu[0])
print(menu[1])
print(menu[2])


name1 =''
name2 =''
name3 =''

name1, name2, name3 = menu #분할 대입 가능
name1, name2, name3 = ('안녕하세요','ㅎㅇ','반갑습니다')

print(name1, name2, name3 )










#전체조회
for  i in  menu:
    print(i)


