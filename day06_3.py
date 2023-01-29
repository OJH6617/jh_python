#파일 읽고 쓰기 함수

#파일만들고 쓰기(txt) #이미 파일이 존재한다면 새로 만들지 않고 쓰기만함
def 파일쓰기():
    f = open('sample.txt','w+',encoding='UTF-8')
    f.write('안녕하세요 반가워요\n')
    f.close()



def 파일읽기():
    f = open('sample.txt','r',encoding='UTF-8')
    # line =f.readline() #한줄을 읽어옴
    lines =f.readlines() #전체를 읽음
    print(lines)
    for line in lines:
        print(line,end=' ')
    f.closed()


#파일 추가로 쓰기
def 파일추가로쓰기():
    f = open('sample.txt','a+', encoding='UTF-8')
    f.write('다시 만나요')
    f.closed()























