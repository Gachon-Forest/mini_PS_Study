''' Date: 2024.07.20
No: 1978
Tier: 브론즈 2
Name: 소수 찾기
Language: 파이썬 '''

n = int(input()) #입력할 수의 개수
num = list(map(int, input().split())) #입력한 수의 개수 값 저장
p = 0 #소수 초기화

for i in num:
    if i == 1: #1은 소수가 아니므로 진행
        continue
    for j in range(2, i): 
        if(i%j==0): #
            break
    else:
        p += 1

print(p)
