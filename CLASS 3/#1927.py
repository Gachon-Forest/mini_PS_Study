''' Date: 2024.08.05
No: 1927
Tier: 실버 2
Name: 최소 힙
Language: 파이썬 '''

import sys
import heapq  # 힙 자료구조를 사용하기 위해 heapq 모듈을 사용
input = sys.stdin.readline

min_heap = [] # 최소 힙을 저장할 리스트를 초기화

for _ in range(int(input())):
    n = int(input())
    
    if n == 0: # 만약 입력된 값이 0이면
        if len(min_heap): # 최소 힙에 요소가 있으면
            print(heapq.heappop(min_heap))  # 최소 힙에서 최솟값을 꺼내 출력
        else:
            print(0) # 최소 힙이 비어있다면 0을 출력
    else:
        heapq.heappush(min_heap, n) # 0이 아니면 그 값을 최소 힙에 추가