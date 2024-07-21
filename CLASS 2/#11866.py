''' Date: 2024.07.21
No: 11866
Tier: 실버 5
Name: 요세푸스 문제 0
Language: 파이썬 '''

import sys

n, k = map(int, sys.stdin.readline().split()) #n, k값 입력받기

idx = 0 #제거되는 사람들의 인덱스 번호
queue = [i for i in range(1, n+1)]
people = [] #제거되는 사람들을 저장할 리스트
while queue:
    idx += k - 1
    if idx >= len(queue): #idx가 쿠의 길이보다 크거나 같으면
        idx %= len(queue) #idx를 뷰의 길이로 나눈 나머지로 저장
    people.append(str(queue.pop(idx))) #큐에서 idx를 제거, res 저장

print("<", ", ".join(people), ">", sep = "")