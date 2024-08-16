''' Date: 2024.08.05
No: 18870
Tier: 실버 2
Name: 좌표 압축
Language: 파이썬 '''

import sys

n = int(input())
inputList = list(map(int,sys.stdin.readline().rstrip().split()))

sortedList = sorted(list(set(inputList))) #위 리스트에서 중복 제거 후 정렬
dictList = dict(zip(sortedList,list(range(len(sortedList))))) #위 리스트에서 각 숫자를 인덱스와 매핑

for x in inputList: 
    print(dictList[x])