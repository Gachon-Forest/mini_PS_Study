''' Date: 2024.08.05
No: 11724
Tier: 실버 2
Name: 연결 요소의 개수
Language: 파이썬 '''

import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline


# 깊이 탐색
def dfs(start, depth):

    #해당 노드 체크 
    visited[start] = True

    # 해당 시작점을 기준으로 계속해서 dfs
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문
visited = [False] * (1 + n)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, n + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1  # 개수를 + 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i, 0)  # dfs탐색
            count += 1  # 개수를 +1

print(count)