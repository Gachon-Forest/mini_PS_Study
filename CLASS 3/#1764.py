''' Date: 2024.07.24
No: 1764
Tier: 실버 4
Name: 듣보잡
Language: 파이썬 '''

n,m = map(int,input().split())
a=set() # a, b 두 집합을 생성
b=set()
result =[] # 결과를 저장할 리스트 초기화
for _ in range(n): # n명의 이름을 받아 집합 a에 추가
    a.add(input())
for _ in range(m): # m명의 이름을 받아 집합 b에 추가
    b.add(input())

for i in a : # a와 b의 교집합을 찾아 result 리스트에 추가
    if i in b :
        result.append(i)
result.sort() # 교집합으로 찾은 이름들을 알파벳 순으로 정렬
print(len(result))
for i in result :
    print(i)