#csv파일 (구 엑셀_)
# import >> 외장모듈 사용
import csv

def csv파일생성():
    f=open('kyobo.csv', 'w', newline='')
    wr = csv.writer(f)
    wr.writerow(['방문자수','판매량'])
    f.closed()

def csv파일이어쓰기():
    f=open('sample.csv', 'a', newline='')
    ad=csv.writer(f)
    ad.writerow([2,'년도','인구'])
    f.closed()

def csv파일읽기():
    f=open('sample.csv','r')
    rd=csv.reader(f)
    for row in rd:
        print(row)  
    f.close()

csv파일생성()
