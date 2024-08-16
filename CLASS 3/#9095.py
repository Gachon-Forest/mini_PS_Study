''' Date: 2024.07.25
No: 9095
Tier: 실버 3
Name: 1, 2, 3 더하기
Language: 파이썬 '''

import sys
input = sys.stdin.readline

def func(x): # x에 대해 특정 수열 값을 계산하는 재귀함수
  if x==1:
    return 1
  elif x==2:
    return 2
  elif x==3:
    return 4
  else:
    return func(x-1)+func(x-2)+func(x-3) # n > 3인 경우, func(x-1), func(x-2), func(x-3)의 합을 반환

t = int(input())
for _ in range(t):
  n = int(input())
  print(func(n))