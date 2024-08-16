''' Date: 2024.08.05
No: 1012
Tier: 실버 2
Name: 유기농 배추
Language: 파이썬 '''

import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

t = int(sys.stdin.readline()) # 테스트 케이스 받는 부분

dx = [-1, 1, 0, 0] # 상하좌우 이동하여 계산하기 위한 list
dy = [0, 0, -1, 1]

def dfs(x, y): #dfs 정의
  if x <= -1 or x >= n or y<= -1 or y>= m:
    return False

  if graph[x][y] == 1: # 현재 위치가 배추가 있는 곳이면
    graph[x][y] = 0 #방문
    #dfs 재귀 호출
    for i in range(4):
      dfs(x + dx[i], y+dy[i])

    return True # 연결된 하나의 컴포넌트를 찾은 경우 True 반환
  return False # 배추가 없는 곳(0)이라면 False 반환

answer = []
for _ in range(t):
  m, n, k = list(map(int, sys.stdin.readline().split()))  # m: 가로 길이, n: 세로 길이, k: 배추의 개수

  graph = [[0]*m for _ in range(n)]
  # 배추의 위치 입력 받아서 그래프에 표시
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1

  cnt = 0 # 컴포넌트 수(필요한 지렁이 수)를 세는 변수
  for i in range(n):
    for j in range(m):
      if dfs(i, j):
        cnt +=1

  print(cnt)