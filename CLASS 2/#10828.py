''' Date: 2024.07.09
No: 10828
Tier: 실버 4
Name: 스택
Language: 파이썬 '''

from sys import stdin

n = int(stdin.readline())
s = [] #데이터를 저장할 스택 공간 생성
for i in range(n):
    a=stdin.readline().split()

    if a[0] == 'push': s.append(a[1]) #push 입력시 값 추가
     
    elif a[0] == 'pop':
        if len(s) == 0: print(-1) #스택안에 값이 없으면 -1출력
        else: print(s.pop())  #있으면 가장 위에 있는 값을 빼내고 해당 값 출력

    elif a[0] == 'size': print(len(s)) #리스트의 길이를 출력

    elif a[0] == 'empty':
        if len(s) == 0: print(1) #리스트의 길이가 0이면 1을 출력
        else: print(0) #아니면 0 출력

    elif a[0] == 'top':
        if len(s) == 0: print(-1) #스택안에 값이 없으면 -1 출력
        else: print(s[-1]) #있으면 가장 위에 있는 값 출력

