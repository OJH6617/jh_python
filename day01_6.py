#input 과 print를 활용하여 만들어 보세요
#이름은 무엇인가요?
#나이는 몇살인가요?    #int()
#성별은 무엇인가요?
#키는 몇인가요? #float

# 이름 = input('이름은 무엇인가요? =')
# 나이 = int(input('나이는 몇살인가요? ='))
# 성별 = input('성별은 무엇인가요? =')
# 키 = float(input('키는 몇인가요? ='))

# print('안녕하세요 제 이름은'+이름+'입니다')
# print('제 나이는',나이,'이고')
# print('제 성별은'+성별+'입니다')
# print('마지막으로 제 키는',키,'입니다')



#2


#10~99사이의 숫자를 입력받아 십의 자리와 일의 자리를 알려주는 프로그램 만들기

#ex 10~99사이의 숫자를 입력하세요 45
#십의자리: (/)
#일의자리: (%)

숫자 = int(input('10~99사이의 숫자를 입력하세요='))
print('십의자리:',int(숫자/10),)
print('일의자리:',int(숫자%10),)
