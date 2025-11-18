'''
    2의 1승 -> 사각형 1개
    2의 2승 -> 사각형 4개
    2의 3승 -> 사각형 16개
    2의 4승 -> 사각형 64개
    
    An = An-1 x 4 개의 Z 개수
'''

'''
    위치 정하기
    N이 주어지면 행과 열의 크기가 정해짐
    r,c가 주어지면 전체 사각형에서 어느 사분면에 위치하는지 알 수 있음
    그렇다면 큰 사각형 범위가 주어짐.
    그 중에서 또 어떤 범위에 존재하는 지 확인
    그렇게 재귀적으로 돌아서 나온 값을 전부 더하면 정답
'''

N, r, c = map(int, input().split())
# print(N, r, c)
ans = 0
now_l = 0
while True:
    if N == 1:
        break
    # 현재 사각형 크기 -> 2**n x 2**n
    now_l = 2 ** N
    # print(N, r, c, ans, now_l, now_l//2)
    # 왼쪽 위부터 오른쪽으로 1, 2, 3, 4
    if 0 <= r < now_l//2 and 0 <= c < now_l//2:
        # 왼쪽 위 사각형에 현재 r,c가 위치
        N -= 1
    elif 0 <= r < now_l//2 and now_l//2 <= c < now_l:
        # 오른쪽 위 사각형
        N -= 1
        ans += (now_l**2)//4 * 1
        c -= now_l//2 # 열 위치 변경
    elif now_l//2 <= r < now_l and 0 <= c < now_l//2:
        # 왼쪽 아래 사각형
        N -= 1
        ans += (now_l**2)//4 * 2
        r -= now_l//2 # 행 위치 변경   
    elif now_l//2 <= r < now_l and now_l//2 <= c < now_l:
        # 오른쪽 아래 사각형
        N -= 1
        ans += (now_l**2)//4 * 3
        r -= now_l//2 # 행 위치 변경
        c -= now_l//2 # 열 위치 변경
# print(N,r,c)
if (r,c) == (0,0):
    print(ans)
if (r,c) == (0,1):
    print(ans+1)
if (r,c) == (1,0):
    print(ans+2)
if (r,c) == (1,1):
    print(ans+3)  

