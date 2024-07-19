''' Date: 2024.07.20
No: 10814
Tier: 실버 5
Name: 나이순 정렬
Language: 파이썬 '''

n = int(input()) #총 회원수 입력받기
user = [] #회원 정보를 저장할 데이터 리스트 생성

for _ in range(n): #사용자의 나이와 이름을 입력받음 
    age, name = input().split()
    user.append([int(age), name])

for i in sorted(user, key=lambda x : x[0]): #나이를 기준으로 오름차순으로 정렬
    print(i[0], i[1])