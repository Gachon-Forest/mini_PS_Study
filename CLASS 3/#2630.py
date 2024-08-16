''' Date: 2024.08.05
No: 2630
Tier: 실버 2
Name: 색종이 만들기
Language: 파이썬 '''

import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
 
result = [] # 색종이의 색상별 개수를 저장할 리스트

def solution(x, y, N) :
  color = paper[x][y] # 현재 영역의 색
  for i in range(x, x+N) : # 현재 영역의 모든 색상이 동일한지 확인
    for j in range(y, y+N) :
      if color != paper[i][j] : # 색상이 다르면
        # 종이를 4개 구역으로 나누어 재귀 호출
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 : # 색상이 모두 같다면 색상에 따라 결과를 추가
    result.append(0)
  else :
    result.append(1)


solution(0,0,N) #분할 정복
print(result.count(0))
print(result.count(1))