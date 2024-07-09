''' Date: 2024.07.08
No: 9012
Tier: 실버 4
Name: 괄호
Language: 파이썬 '''

a= int(input())

for i in range(a):
    stack=[] #괄호를 넣을 스택 설정
    a=input() #a의 값을 입력받음
    for j in a: 
        if j == '(': # (가 입력되면 스택에 추가
            stack.append(j)
        elif j == ')': # )가 입력되면 스택에서 빼낸다
            if stack:
                stack.pop()
            else: #스택에 괄호가 없을경우 NO
                print("NO")
                break
    else:
        if not stack: #break문으로 안끊기고 스택이 비어있다면 YES
            print("YES")
        else: #아니면 NO
            print("NO")