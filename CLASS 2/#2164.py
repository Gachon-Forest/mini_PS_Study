''' Date: 2024.07.12
No: 2164
Tier: 실버 4
Name: 카드2
Language: 파이썬 '''

from collections import deque

N = int(input()) #카드 총 개수 
deque = deque([i for i in range(1, N+1)]) #1부터 N까지의 숫자를 가지는 덱 생성

while(len(deque) >1): #덱의 길이가 1보다 클 동안 반복문 실행
    deque.popleft() #덱의 왼쪽 요소 제거
    num = deque.popleft()
    deque.append(num) #오른쪽 끝에 추가
    
print(deque[0]) #마지막 남은 카드 번호 출력
