''' Date: 2024.07.20
No: 1259    
Tier: 브론즈 1
Name: 팰린드롬수 
Language: 파이썬 '''

while True:
    a= input() #값 입력
    if a == "0": #0이 입력되면 루프를 빠져나온다
        break
    elif a == a[::-1]: #a의 뒤집어진 수와 a의 값이 같으면 yes를 출력
        print("yes")
    else:
        print("no")