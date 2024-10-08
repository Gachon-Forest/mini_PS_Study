''' Date: 2024.08.05
No: 2805
Tier: 실버 2
Name: 나무 자르기
Language: 파이썬 '''

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    #벌목 높이를 이분탐색
    if log >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)