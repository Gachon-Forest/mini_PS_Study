''' Date: 2024.07.20
No: 30802  
Tier: 브론즈 3
Name: 웰컴키트
Language: 파이썬 '''

'''티셔츠 사이즈 6개 T장의 묶음
   펜은 P자루씩 묶음으로 주문 혹은 한 자루
   입력: 첫줄 참가자 수 N, 둘째 줄 티셔츠 사이즈 별 신청자의 수, 셋째 줄: 정수 티셔츠와 펜의 묶음 수 의미 정수 T, P 주어짐
   출략: T장씩 최소 몇 묶음, P자루씩 최대 몇 묶음, 한 자루씩 몇 개'''

import sys

input = sys.stdin.read
data = input().split() #입력된 데이터 리스트로 저장

n = int(data[0]) #참가자 수 파악
size = list(map(int, data[1:7])) #티셔츠 사이즈 별 개수 저장
t = int(data[7]) #티셔츠 개수와
p = int(data[8]) #펜의 묶음 수

min = 0 #최소 값 
for i in size:
    if i % t == 0: #티셔츠 한 묶음으로 티셔츠 별 신청자의 수
        min += i // t #나누어 떨어지면 몫을 더함 
    else: 
        min += i // t + 1 #나누어 떨어지지 않으면 몫에 1을 더한 후 저장
    
print(min) #티셔츠 최소 묶음 수 출력
print(n//p, n%p) #펜 최대 묶음 수, 묶음 당 개수 