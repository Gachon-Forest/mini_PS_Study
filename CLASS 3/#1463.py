''' Date: 2024.07.25
No: 1463
Tier: 실버 3
Name: 1로 만들기
Language: 파이썬 '''

n = int(input())

dp = [0] * 10000001 #dp 테이블 초기화

#다이나믹 프로그래밍 
for i in range (2, n+1) :
    dp[i] = dp[i-1] + 1 #1을 빼주는 경우
    if i % 2 == 0: # 2로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//2] + 1) 
    
    if i % 3 == 0 :# 3으로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])