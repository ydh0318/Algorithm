# G3-29703 펭귄의 하루

'''
    NxM 의 행렬로 나누어져

    펭귄은 위험구역(D)이 아닌 곳을 상하좌우로 이동한다.

    물고기 서식지 중 최소한 한 곳을 들러 사냥을 마치고 집으로 돌아가려 한다.
    펭귄이 사냥하는 데 걸리는 시간은 고려하지 않고, 출발 지점에서 물고기들의
    서식 구역을 들르지 않아도 펭귄이 사는 집을 지나갈 수 있다.

    또한 물고기들이 서식하는 구역을 들른 후에 펭귄이 출발한 지역을 거쳐
    돌아갈 수 있음.


    S 시작, H 집, E 안전구역, D 위험구역, F 물고기 서식지    
'''
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_char):
    dist = [[-1] * M for _ in range(N)]
    q = deque()
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == start_char:
                q.append((i, j))
                dist[i][j] = 0
                
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i][0], c + dr[i][1]
            if 0 <= nr < N and 0 <= nc < M:
                if grid[nr][nc] != 'D' and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    
    return dist

N, M = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]

# 1. 시작점(S)에서 각 칸(서식지 포함)까지의 최단거리 구하기
dist_from_S = bfs('S')

# 2. 집(H)에서 각 칸(서식지 포함)까지의 최단거리 구하기 (H에서 역탐색)
dist_from_H = bfs('H')

ans = float('inf')

for i in range(N):
    for j in range(M):
        # 3. 서식지(F)일 때, 거리를 더해서 최솟값 갱신
        if grid[i][j] == 'F':
            # 둘 중에 하나라도 갈 수 없다면 구하지 못한 것이므로 제외
            if dist_from_S[i][j] != -1 and dist_from_H[i][j] != -1:
                ans = min(ans, dist_from_S[i][j] + dist_from_H[i][j])

# 하나라도 갈 수 있는 경로가 없었다면 -1 리턴
if ans == float('inf'):
    print(-1)
else:
    print(ans)