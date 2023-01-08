# 20이상은 성인
# 14세 이상은 청소년
# 14세 미만은 어린이

# 나이 = int(input('나이를 입력하세요.'))

# if 나이 >= 20:
#     print('성인입니다.')
# elif 나이 <20 and 나이 >=14 :
#     print('청소년입니다.')
# else :
#     print('어린이입니다.')


나이 = int(input('나이를 입력하세요.'))
if 나이 >= 23:
    print('회사원')
elif 나이>=20:   #elif의 특징은 위에거가 이미 틀렸을 때  실행되는 것 임 그래서 and 나이<=23 이 필요가 없음 
    print('대학교')
elif 나이>=17:
    print('고등학교')
elif 나이 >=14:
    print('중학교')
elif 나이 >=8:
    print('초등학교')
elif 나이>=0:
    print('유치원')
else:
    print('??????')


