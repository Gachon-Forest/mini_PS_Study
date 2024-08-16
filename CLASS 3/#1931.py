''' Date: 2024.08.08
No: 1931
Tier: 실버 1
Name: 회의실 배정
Language: 파이썬 '''

import sys
n = int(sys.stdin.readline())
timeline = [] # 회의 일정을 저장할 리스트 초기화
for i in range(n):
    start, end = map(int,sys.stdin.readline().split()) # 회의의 시작 시간과 종료 시간을 입력받음
    timeline.append((start, end)) # 튜플로 저장하여 리스트에 추가

timeline.sort(key=lambda x : (x[1],x[0])) # 회의 일정을 종료 시간을 기준으로 오름차순 정렬, 종료 시간이 같으면 시작 시간을 기준으로 정렬
# 회의의 최대 개수를 세기 위한 변수 초기화
count = 1
end = timeline[0][1]
# 나머지 회의들에 대해 반복
for i in range(1, n):
    if timeline[i][0]>=end:
        end = timeline[i][1] # 종료 시간을 갱신
        count += 1 # 회의 개수 증가

print(count)