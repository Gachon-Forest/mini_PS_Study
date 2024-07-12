''' Date: 2024.07.12
No: 1546
Tier: 브론즈 1
Name: 평균
Language: 파이썬 '''

n=int(input()) #과목 개수 
test = list(map(int, input().split())) #테스트 점수 
max=max(test) #최고 점수 

new=[] #새 리스트 생성
for score in test:
    new.append(score/max*100) #점수/최고점*100의 값 리스트에 추가
avg=sum(new)/n #평균 계산
print(avg) #평균 출력
