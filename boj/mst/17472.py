from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
# 상하좌우
dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
queue = deque()
visited = set()
num_grid = [[0] * M for _ in range(N)]

cnt = 1
for i in range(N):
    for j in range(M):
        # 육지 발견
        if grid[i][j] == 1:
            # 아직 방문하지 않은 육지면 cnt 추가 함.
            if num_grid[i][j] == 0:
                # 좌표 집어 넣음
                queue.append((i, j))
                while queue:
                    r, c = queue.popleft()
                    # 육지 번호 표시
                    num_grid[r][c] = cnt
                    for k in range(4):
                        nr, nc = r + dr[k][0], c + dr[k][1]
                        # 육지이고 아직 방문하지 않은 곳
                        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1 and num_grid[nr][nc] == 0:
                            queue.append((nr, nc))
                cnt += 1
            # 상하좌우로 확인하며 진행 가능하면 큐에 집어넣음.
            for k in range(4):
                nr, nc = i + dr[k][0], j + dr[k][1]
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                    q.append((i, j, k, 0, num_grid[i][j]))
num_island = cnt
# for v in num_grid:
#     print(v)
# print(cnt)

# bfs로 순회하며 최단거리 확인.
# 각 진행 방향으로 순회해서 육지 만나면 최단거리 업데이트 함.
candidate = []
while q:
    # 행, 열, 현재 진행 방향, 현재 다리 길이
    row, col, now_dr, now_sum, start_island = q.popleft()
    # 진행 방향으로 위치 업데이트
    nrow, ncol = row + dr[now_dr][0], col + dr[now_dr][1]
    # 범위 안인지 확인
    if 0 <= nrow < N and 0 <= ncol < M:
        # 육지 만났는지 확인
        if num_grid[nrow][ncol] != 0:
            if now_sum >= 2:
                candidate.append((now_sum, start_island, num_grid[nrow][ncol]))
        else:
            # 바다이면 계속 순회
            q.append((nrow, ncol, now_dr, now_sum+1, start_island))


# union find 이용해서 1.집합에 모든 섬이 다 들어가는지 확인하며 최단거리를 구함.
parents = list(range(num_island))
rank = [0] * (num_island)

def find(x, parents):
    # 확인하고 있는 노드의 부모가 자기 자신이 아니라면,
    if parents[x] != x:
        # 부모 노드 찾으러 감.
        parents[x] = find(parents[x], parents)
    return parents[x]

def union(x,y):
    px = find(x,parents)
    py = find(y,parents)

    if px != py: # 부모가 다르면 합 집합 수행함.
        if rank[px] > rank[py]: # x의 부모의 랭크(길이)가 더 길면 여기 붙임
            parents[py] = px
        elif rank[py] > rank[px]: # x의 부모의 랭크(길이)가 더 길면 여기 붙임
            parents[px] = py
        else: # 둘다 같으면 아무데나 붙임
            parents[py] = px
            rank[px] += 1

candidate.sort()
ans = 0
mst = []
# 후보군 돌면서 구함.
for dist, s, e in candidate:
    # 하나의 집합에 있지 않은 경우
    if find(s,parents) != find(e,parents):
        union(s,e)
        ans += dist

for i in range(1,num_island):
    find(i,parents)

print(ans) if len(set(parents)) == 2 else print(-1)