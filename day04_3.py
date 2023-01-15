cafe_menu=['아메리카노']

#append를 사용하여 카페메뉴 이름 추가

#전체 출력
cafe_menu.append('카페라떼')
cafe_menu.append('아이스티')
cafe_menu.append('녹차라떼')
cafe_menu.append('케이크')
for i in cafe_menu:
    print(i)



#데이터 갯수 len
리스트의갯수=len(cafe_menu)
print(리스트의갯수)

#수정
cafe_menu[0] ='에스프레소' #0번방에 있는 아메리카노를 에스프레소로 바꾸겠다.
print(cafe_menu)


