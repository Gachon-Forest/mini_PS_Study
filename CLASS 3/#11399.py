''' Date: 2024.07.24
No: 11399
Tier: 실버 4
Name: ATM
Language: 파이썬 '''

n = int(input())  # 첫째줄 입력
peoples = list(map(int, input().split()))  # 기다리는 사람들 리스트로 입력 받음

peoples.sort()  # 작은 순서대로 정렬
answer = 0  # 정답 변수를 0으로 만듬

for x in range(1, n+1):
    answer += sum(peoples[0:x])  # 리스트의 0번째 수부터 x번째 수까지를 더해줌
print(answer)  # 정답 제출