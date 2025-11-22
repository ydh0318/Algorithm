from collections import deque

n,m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# start = [0,0]
q = deque()

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            dp[i][j] = 0
            q.append((i,j,0))
            visited[i][j] = True
            break
        
dr = [(-1,0),(1,0),(0,-1),(0,1)]

while q:
    r,c,v = q.popleft()
    for i in range(4):
        nr, nc = r+dr[i][0], c+dr[i][1]
        # 범위 안이고, 갈 수 있는 곳
        if 0<=nr<n and 0<=nc<m and grid[nr][nc] == 1:
            # 아직 방문하지 않은 곳이면
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dp[nr][nc] = v+1
                q.append((nr,nc,v+1))

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and dp[i][j] == 0:
            dp[i][j] = -1

for i in range(n):
    for j in range(m):
        print(dp[i][j], end=' ')
    print()


        