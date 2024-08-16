''' Date: 2024.08.08
No: 1074
Tier: 실버 1
Name: Z
Language: 파이썬 '''

import sys
sys.setrecursionlimit(10**3) # 재귀 호출 한도를 설정

# N: 배열의 크기를 결정하는 변수
# r: 목표 행 위치
# c: 목표 열 위치
N, r, c = map(int,input().split())
size = 2**N #배열의 크기

def dfs(row, col, n, value):
    n = n // 2

    if row < n and col < n: #1사분면
        if n == 1:
            print(value)
            exit(0)
        dfs(row, col, n, value)

    elif row < n and col >= n: #2사분면
        if n == 1:
            print(value + 1)
            exit(0)
        dfs(row, col - n, n, value + n ** 2)

    elif row >= n and col < n: #3사분면
        if n == 1:
            print(value + 2)
            exit(0)
        dfs(row - n, col, n, value + n ** 2 * 2)

    elif row >= n and col >= n: #4사분면
        if n == 1:
            print(value + 3)
            exit(0)
        dfs(row - n, col - n, n, value + n ** 2 * 3)

dfs(r,c,size,0)