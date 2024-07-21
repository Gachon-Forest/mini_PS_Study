''' Date: 2024.07.21
No: 1018
Tier: 실버 4
Name: 체스판 다시 필하기
Language: 파이썬 '''

n,m=map(int,input().split())

a=[] #체스판의 정보 저장할 리스트
b=[] #변경 횟수를 저장할 리스트
for i in range(n):
    a.append(input())
    
for q in range(n-7): #8*8을 만들기 위함 
    for r in range(m-7):
        w_index=0 #흰색으로 시작
        b_index=0 #검은색으로 시작
        for i in range(q,q+8): #행 반복
            for j in range(r,r+8): #열 반복
                if (i+j)%2==0: #위치가 짝수일 때
                    if q[i][j]!='W':#검은색이면
                        w_index+=1 #W로 칠하는 갯수 증가
                    else: #하얀색이면
                        b_index+=1 #B로 칠하는 갯수 증가
                else: #홀수인 경우
                    if q[i][j]!='W':
                        b_index+=1
                    else:
                        w_index+=1
                        
        b.append(w_index) #흰색으로 시작할 때 변경 횟수 추가
        b.append(b_index) #거은색으로 시작할 때 변경 횟수 추가
print(min(b)) #최솟값 출력