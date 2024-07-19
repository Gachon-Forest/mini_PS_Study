''' Date: 2024.07.20
No: 11050
Tier: 브론즈 1
Name: 이항계수 1
Language: 파이썬 '''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def factorial(n): #재귀함수 사용
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(n) // (factorial(n-k)*factorial(k))) #조합 공식