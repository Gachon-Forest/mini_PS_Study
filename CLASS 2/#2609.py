''' Date: 2024.07.20
No: 2609
Tier: 브론즈 1
Name: 최대공약수와 최소 공배수
Language: 파이썬 '''

#모듈 사용하기
''' import math

a, b = map(int, input().split())

print(math.gcd(a,b))
print(math.lcm(a,b)) '''

a, b = map(int, input().split()) #두 수 입력받기 

def gcd(a, b): #최대공약수를 적용할 함수 생성
    while b > 0: #b가 0보다 크면 
        a, b = b, a % b #a에 b의 값을 저장하고 b에 a와 b를 나눈 값의 나머지를 저장
    return a

def lcm(a, b): #최소공배수를 적용할 함수 생성
    return a * b // gcd(a, b) #두 수 의 곱을 최대공약수로 나눔

print(gcd(a, b))
print(lcm(a, b))