while True:
    re=list(map(int, input().split())) #세 변의 값을 입력 받을 리스트를 생성
    if re[0] ==0 and re[1]==0 and re[2]==0: #세 변의 값이 전부 0이면 활동을 끝냄
        break
    re.sort() #리스트 안의 값 정렬
    if re[2]**2==re[0]**2+re[1]**2: #피타고라스 정리 
        print("right")
    else:
        print("wrong")