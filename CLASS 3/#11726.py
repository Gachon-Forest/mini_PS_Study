''' Date: 2024.07.25
No: 11726
Tier: 실버 3
Name: 2xn 타일링
Language: 파이썬 '''

n = int(input())

dp = [0 for _ in range(n+1)] 

# n이 3 이하일 경우는 별도의 계산 없이 n을 출력
if n <= 3 : print(n)
else : 
	dp[1] = 1 # dp[1]은 1을 채우는 방법의 수: 1가지
	dp[2] = 2 # dp[2]는 2를 채우는 방법의 수: 2가지 (1x2, 2x1 타일 2개)
	# 3부터 n까지의 값을 동적 계획법으로 계산
	for i in range(3, n+1):
		dp[i] = dp[i-1] + dp[i-2]

	print(dp[i]%10007)
		