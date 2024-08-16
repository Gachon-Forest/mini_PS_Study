''' Date: 2024.07.24
No: 11723
Tier: 실버 5
Name: 집합
Language: 파이썬 '''

import sys

m = int(sys.stdin.readline()) 
s = set() #s를 초기화

for _ in range(m): 
    temp = sys.stdin.readline().strip().split()
    
    #명령어가 한 단어 일 경우
    if len(temp) == 1:
        if temp[0] == "all": #all 명령어
            s = set([i for i in range(1, 21)])
        else: #empty 명령어
            s = set() #빈 집합으로 초기화
    
    else: #명령어가 두 단어일 경우
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add": 
            s.add(x)
        elif func == "remove":
            s.discard(x)
        elif func == "check":
            print(1 if x in s else 0)  # s에 x가 있으면 1, 없으면 0을 출력
        elif func == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)