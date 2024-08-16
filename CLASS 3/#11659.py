''' Date: 2024.07.25
No: 11659
Tier: 실버 3
Name: 구간 합 구하기 4
Language: 파이썬 '''

import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n: 수열의 크기, m: 구간 합을 구할 횟수
arr = [0] #수열을 저장할 리스트
arr += list(map(int, input().split())) # 수열의 각 값을 입력받아 리스트에 추가

for i, num in enumerate(arr): 
  if i>0: #첫 번째 요소는 무시
    arr[i] = arr[i-1] + num 
#m개의 구간에 대해 구간 합을 계산 
for _ in range(m): 
  i,j = map(int, input().split())
  print(arr[j] - arr[i-1])