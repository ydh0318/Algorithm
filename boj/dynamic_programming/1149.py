'''
    RGB거리에는 집이 N개 있다.
    거리는 선분으로 나타내고 1~N번 집이 순서대로 있다.
    
    각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때
    모든 집을 칠하는 비용의 최솟값을 구해보자.
    
    1. 1번집의 색은 2번 집의 색과 같이 않아야 함.
    2. N번 집의 색은 N-1번 집의 색과 같지 않아야 함.
    3. i(2 <= i <= N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 함.
'''

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

for i in range(1,N):   
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
    
print(min(dp[-1]))
