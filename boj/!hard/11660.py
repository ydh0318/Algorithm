N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
ops = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = grid[0][0]

for row in grid:
    print(row)
print()

for i in range(N):
    for j in range(N):
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] = grid[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        elif i == 0:
            dp[i][j] = grid[i][j] + dp[i][j-1]
        elif j == 0:
            dp[i][j] = grid[i][j] + dp[i-1][j]

for row in dp:
    print(row)

# for x1,y1,x2,y2 in ops:
#     # x2,y2까지의 부분 합에서 포함되지 않은 부분을 빼야함.
#     if x1 == x2 and y1 == y2:
#         print(grid[x1-1][y1-1])
#         continue
#     if x1 > 1 and y1 > 1:
#         print(dp[x2-1][y2-1]-dp[x2-1][y1-1-1]-dp[x1-1-1][y2-1]+dp[x1-1-1][y1-1-1])
#     else: # 하나라도 1인 경우
#         # 행끼리 같은경우
#         if x1 == 1 and y1 == 1:
#             print(dp[x2-1][y2-1])
#         elif x1 == 1 and y1 != 1: # 0행 고정
#             print(dp[x2-1][y2-1]-dp[x2-1][y1-1])
#         elif y1 == 1 and x1 != 1: # 0열 고정
#             print(dp[x2-1][y2-1]-dp[x1-1][y2-1])

for x1, y1, x2, y2 in ops:
    x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
    if x1 == 0 and y1 == 0:
        print(dp[x2][y2])
    elif x1 == 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    elif y1 == 0:
        print(dp[x2][y2] - dp[x1-1][y2])
    else:
        print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])