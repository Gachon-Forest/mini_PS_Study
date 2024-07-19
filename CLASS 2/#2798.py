''' Date: 2024.07.20
No: 2798
Tier: 브론즈 2
Name: 블랙잭
Language: 파이썬 '''

n, m  = map(int, input().split()) #n, m의 값 입력 받기
card = list(map(int, input().split())) #카드 값 입력 받은 후 리스트로 저장
num = 0

for i in range(n): #3중 for문을 돌려 세 카드의 값을 랜덤으로 받고 그 값이 겹치지 않게 함
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] > m: #3 카드의 값이 m보다 크면 건너뛰기
                continue
            else:
                num = max(num, card[i] + card[j] + card[k]) #아니라면 num에 가장 큰 값을 저장 
print(num)
