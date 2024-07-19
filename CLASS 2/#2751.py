''' Date: 2024.07.20
No: 2751
Tier: 실버 5
Name: 수 정렬하기 2
Language: 파이썬 '''

import sys
input=sys.stdin.readline

n=int(input())
list=[] #값 저장할 리스트 생성

for i in range(n):
    list.append(int(input()))

for i in sorted(list): #파이썬에서 제공하는 정렬기능 사용
    print(i)
