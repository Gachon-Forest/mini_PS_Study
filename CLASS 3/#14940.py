''' Date: 2024.08.08
No: 14940
Tier: 실버 1
Name: 쉬운 최단거리
Language: 파이썬 '''

import sys
from collections import deque
input = sys.stdin.readline

direction = [(-1,0),(1,0),(0,-1),(0,1)] #방향 벡터
n,m = map(int,input().split()) #행, 열 개수 입력 받기
arr = list(input().split() for _ in range(n)) #2차원 리스트
visited = [[False]*m for _ in range(n)] #방문 여부 체크
ans = [[0]*m for _ in range(n)] #최단 거리 저장
for i in range(n): #시작 지점 찾기
    for j in range(m):
        if arr[i][j]=="2":
            visited[i][j] = True
            q = deque([(i,j)])

while q: #bfs 시작
    x, y = q.popleft()
    for dx, dy in direction:
        nx = x+dx
        ny = y+dy

        if 0<=nx<n and 0<=ny<m and arr[nx][ny]=="1" and not visited[nx][ny]:
            q.append((nx,ny))
            visited[nx][ny] = True
            ans[nx][ny]= ans[x][y]+1

for i in range(n): #결과 출력
    for j in range(m):
        if not visited[i][j] and arr[i][j]=="1":
            print(-1,end=" ")
        else:
            print(ans[i][j], end=" ")
    print()