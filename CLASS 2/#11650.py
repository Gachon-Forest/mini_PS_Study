''' Date: 2024.07.20
No: 11650
Tier: 실버 5
Name: 좌표 정렬하기
Language: 파이썬 '''

n=int(input()) 

list=[]

for i in range(n):
    [a, b] = map(int, input().split())
    list.append([a, b])

list.sort()
for i in list:
    print(i[0], i[1])

#수 정렬과 설명 동일 다른점은 x, y좌표를 구분하기 위해 이중 리스트를 사용했다 정도