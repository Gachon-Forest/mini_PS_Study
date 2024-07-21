''' Date: 2024.07.21
No: 10816
Tier: 실버 4
Name: 숫자 카드 2
Language: 파이썬 '''

'''입력
   첫번째 줄: 상근이가 가지고 있는 숫자 카드의 개수 N
   두번째 줄: 숫자 카드에 적혀있는 정수
   세번째 줄: M이 주어짐
   네번째 줄: 숫자카드를 몇개 가지고 있어야 하는지 구해야할 M개의 정수
   출력
   입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자카드를 몇 개 가지고 있는지'''

import sys
input = sys.stdin.readline

#각각 입력 받을 값의 변수 설정
n = int(input())
card = list(map(int, input().split()))
m = int(input())
min = list(map(int, input().split()))

card.sort() #카드 리스트를 정렬

dic = {} #딕셔너리 설정

#i가 딕셔너리 안에 존재하면 dic[i] 값 증가, 아니면 1로 설정
for i in card: 
    if i in dic:
        dic[i] +=1
    else:
        dic[i] =1

#i가 딕셔너리 안에 존재하면 dic[i] 값 출력, 아니면 0 출력
for i in min:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print("0", end = " ")