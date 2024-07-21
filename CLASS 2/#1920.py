''' Date: 2024.07.21
No: 1920
Tier: 실버 4
Name: 수 찾기
Language: 파이썬 '''

#각각 입력받아야 할 값의 변수 설정
n = int(input()) 
a = set(map(int, input().split()))
m = int(input())
l = list(map(int, input().split()))

for num in l:
    if num in a: #num이 집합 a에 존재하면 
        print(1) #1 출력
    else: #아니면
        print(0) #0 출력