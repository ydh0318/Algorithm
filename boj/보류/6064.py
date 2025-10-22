'''
    카잉제국의 백성들은 특이한 달력은 사용한다.
    
    그들은 M과 N보다 작거나 같은 두개의 자연수 x,y를 가지고
    각 년도를 <x:y>와 같은 형식으로 표현하였다.
    그들은 이 세상의 시초에 해당하는 첫 번째 해를 <1:1>로 표현하고, 
    두 번째 해를 <2:2>로 표현하였다.
    
    <x:y>의 다음 해를 표현한 것을 <x`:y`>라고 하자
    만일 x < M이면 x`= x + 1 이고, 그렇지 않으면 x` = 1 이다
    y도 마찬가지
    
    <M:N>은 그들 달력의 마지막 해
'''

'''
    M = 10, N = 12일 때 달력 표현법
    (1,1) -> (2,2) -> (3,3) -> (4,4) -> (5,5) ->
    (6,6) -> (7,7) -> (8,8) -> (9,9) -> (1,10) ->
    (1,11) -> (2,12) -> (3,1) ... -> (5,1) -> ... ->
    (7,1) -> ... -> ()
    
    M과 N의 차이 만큼 초기화 된다.
    
    1. 나올 수 있는지 판별
    2. 몇번째 나오는지 구함
    
'''
# 틀코
# t = int(input())

# for _ in range(t):
#     # print()
#     M, N, x, y = map(int, input().split())
    
#     i, j = 0, 0
#     cnt = 0
#     ans = -1
#     while True:
#         i = i%M + 1
#         j = j%N + 1
#         cnt += 1
#         print(i,j,cnt)
#         if i == x and j == y: ans = cnt
#         if i == M and j == N: break
#     print(ans)

def find_lcm(a,b):
    for i in range(max(a,b), a*b + 1):
        if i % a == 0 and i % b == 0: return i

t = int(input())

for _ in range(t):
    M, N, x, y = map(int, input().split())
    ans = -1
    
    lcm = find_lcm(M,N)
    # print(lcm)
    
    xcycle = set()
    for i in range(x, lcm+1, M):
        xcycle.add(i)
        
    ycycle = set()
    for i in range(y, lcm+1, N):
        ycycle.add(i)
    
    # xcycle = list()
    # for i in range(x, lcm, M):
    #     xcycle.append(i)
        
    # ycycle = list()
    # for i in range(y, lcm, N):
    #     ycycle.append(i)
        
    # print(xcycle,ycycle)
    if xcycle & ycycle: print(min(list(xcycle & ycycle))) 
    else: print(-1)