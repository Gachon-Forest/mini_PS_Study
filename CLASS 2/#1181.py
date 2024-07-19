''' Date: 2024.07.20
No: 1181
Tier: 실버 5
Name: 단어 정렬
Language: 파이썬 '''

n = int(input())

w = [str(input()) for i in range(n)] #입력한 단어를 저장할 리스트 생성

w = list(set(w)) #중복 제거
w.sort() #abc 순으로 정렬
w.sort(key=len) #단어의 길이가 짧은순으로 정렬

for i in w:
    print(i)