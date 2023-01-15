#문자열을 저장하는 리스트
lst=[]
num=0
#사용자에게 입력을 받아 리스트를 구성
#1: 추가하기 2:수정하기 3:삭제하기 4:전체보기
while True:
    num=int(input('1:추가 2:수정 3:삭제 4:조회'))
    if num==1:
        A=(input('추가할 내용을 입력하세요>>'))
        lst.append(A)          #값을 축사
    elif num==2:
        B=(input('무엇을 수정하시겠습니까?>>'))       #값을 수정(수정하고자 하는 값, 수정할 값)
        E=lst.index(B)
        C=(input('수정 내용을 입력하세요>>'))
        lst[E]=C
    elif num==3:
        D=(input('삭제 내용을 입력하세요>>')) 
        lst.remove(D)         #삭제할 값 입력 (외부에서)
    elif num==4:
        for i in lst:
            print(i)         #전체조회
    elif num==0:
        break
    else:
        print('없는 번호입니다.')
