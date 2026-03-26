import sys

sys.stdin = open('sample_input2.txt', 'r')

tc = int(input())

'''
    지도의 각 셀들은 육지, 또는 바다로 이루어져 있음.
    서로 인접한 1 x 1 크기의 육지 셀들이 모여 하나의 섬을 이룸.
    섬은 직사각형 혹은 정사각형의 모양으로 주어진다.
    
    다리의 건설 규칙은 다음과 같음.
    
    1. 다리의 폭은 항상 1 이고, 가로 또는 세로 방향으로 건설 할 수 있음.
    2. 한개의 다리는 항상 두개의 섬을 연결 할 수 있고, 다리는 반드시 직선으로만 건설 할 수 있다.
    3. 두개의 섬을 연결 할 때, 두 섬의 해안선과 모두 직교하는 방향으로 다리를 연결해야 한다. 
    -> 진행 방향에 섬이 존재해야 함. 이어지는 4번과 연관 됨.
    
    4. 다리는 섬 또는 다른 다리와 인접한 셀을 지나갈 수 있다.
    5. 다리는 동일한 좌표 셀을 중복으로 지나갈 수 있다.
    
    지도 정보가 주어질 때, 지도에 있는 모든 섬을 연결하는 최소 다리건설 비용을 출력하라.
    단, 모든 섬을 연결 할 수 없을 경우, -1을 출력한다.
'''

'''
    지도의 크기 N은 5 이상 10 이하의 정수
    섬의 개수는 2 개 이상 6 개 이하이다.
    지도의 존재하는 임의의 두 섬은 가로 또는 세로 방향으로 2칸 이상이 무조건 떨어짐을 보장한다.
'''

'''
    check_island : 각 섬에 대해 연결된 가장 짧은 거리를 저장하는 리스트
    각 섬의 해안선에서 출발하여 직선으로 이동해야 함.
    상하좌우 중 하나의 방향으로만 이동 가능하며 육지를 만나거나 범위를 벗어 날 경우 종료됨.
    
    반복문을 전부 돌면서 1(육지)를 만나면 진행할 수 있는 방향을 모조리 큐에 집어 넣음 (열, 행, 진행방향, 현재다리길이, 시작 섬 번호)
    그 다음에 bfs 순회로 육지 만나면 종료
    
    육지 개수도 bfs로 찾아야 함.
'''
from collections import deque

for t in range(1, tc+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 상하좌우
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    queue = deque()
    visited = set()
    num_grid = [[0] * N for _ in range(N)]

    cnt = 1
    for i in range(N):
        for j in range(N):
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
                            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1 and num_grid[nr][nc] == 0:
                                queue.append((nr, nc))
                    cnt += 1
                # 상하좌우로 확인하며 진행 가능하면 큐에 집어넣음.
                for k in range(4):
                    nr, nc = i + dr[k][0], j + dr[k][1]
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                        q.append((i, j, k, 0, cnt-1))
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
        if 0 <= nrow < N and 0 <= ncol < N:
            # 육지 만났는지 확인
            if num_grid[nrow][ncol] != 0:
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

    if len(set(parents)) == 2:
        print(f'#{t} {ans}')
    else:
        print(f'#{t} -1')




