''' Date: 2024.07.09
No: 10845
Tier: 실버 4
Name: 큐 
Language: 파이썬 '''

from sys import stdin

n = int(stdin.readline())
q = [] #데이터를 저장할 큐 공간 생성
for i in range(n):
    a=stdin.readline().split()

    if a[0] == 'push': q.append(a[1]) #push 입력시 값 추가
     
    elif a[0] == 'pop':
        if q: print(q.pop(0)) #가장 앞에 있는 값을 빼고 출력
        else: print(-1) #데이터가 없으면 -1 출력

    elif a[0] == 'size': print(len(q)) #리스트의 길이를 출력

    elif a[0] == 'empty':
        if len(q) == 0: print(1) #리스트의 길이가 0이면 1을 출력
        else: print(0) #아니면 0 출력

    elif a[0] =='front':
        if len(q) == 0: print(-1) #큐 안에 값이 없으면 -1 출력
        else: print(q[0]) #아니면 가장 앞에 있는 값 출력

    elif a[0] =='back': 
        if len(q) == 0:print(-1) 
        else: print(q[-1]) #가장 뒤에 있는 값 출력
