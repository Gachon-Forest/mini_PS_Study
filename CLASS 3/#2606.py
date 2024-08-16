''' Date: 2024.07.25
No: 2606
Tier: 실버 3
Name: 바이러스 
Language: 파이썬 '''

import sys
n = int(sys.stdin.readline()) #컴퓨터의 갯수
k = int(sys.stdin.readline()) #연결된 쌍의 갯수
graph = [[] for _ in range(n+1)] 
for i in range(k):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
count = 0
visited = [False]*(n+1)
#DFS 알고리즘
def dfs(x):
    global count
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            count+=1
            dfs(i)

dfs(1)
print(count)