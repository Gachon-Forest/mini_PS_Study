''' Date: 2024.08.08
No: 1697
Tier: 실버 1
Name: 숨바꼭질
Language: 파이썬 '''

from collections import deque

def bfs(): #bfs 정의
    q=deque() #큐 생성
    q.append(n) #초기 위치 추가
    while q:
        x = q.popleft() #큐 가장 앞에 있는 요소 꺼냄
        if x == k: #현재 위치가 동생과 같으면
            print(dist[x]) #이동 횟수 출력
            break
        for r in (x-1, x+1, x*2): # x-1, x+1, x*2 위치를 탐색
            if 0 <= r <=max and not dist[r]: # r이 이동 가능한 범위 내에 있고 아직 방문하지 않았다면
                dist[r] = dist[x] + 1 # 이동 횟수 기록 후 
                q.append(r) #큐에 추가
max = 10 **5 #최대 이동 가능 범위 설정
dist = [0] * (max+1)
n, k = map(int, input().split())
bfs()