# 1520 - 내리막 길
# 260404

'''
    여행을 떠난 세준이는 지도를 하나 구하였다.
    이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.

    한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 
    각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.

    현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 가장 오른쪽 아래 칸으로 가려고 한다
    그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하려고 한다.

    지도가 주어질 때, 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성
'''

'''
    중복 경로를 막기 위해 dp를 사용
    dp는 M x N크기의 경로의 수를 저장해놓은 테이블
    가면서 다른 경로가 있으면 더함.
    만약 해당 위치에 이미 dp테이블의 값이 저장되어 있으면
    내 위치의 dp값을 더해주고 return
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [(-1,0),(1,0),(0,-1),(0,1)]
M, N = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
# print(grid)

def dfs(r,c):
    # 목적지는 갈 수 있는 곳이 없어서 1로 초기화
    if (r,c) == (M-1,N-1): return 1
    
    # 이미 dp테이블에 계산되어 있으면 더 갈 필요 없이 그대로 값 리턴
    if dp[r][c] != -1: return dp[r][c]

    # 처음 방문하는 곳이면 계산 시작
    dp[r][c] = 0 # 우선 방문 표시
    for i in range(4):
        nr, nc = r + dr[i][0], c + dr[i][1]
        if 0 <= nr  < M and 0 <= nc < N: # 범위 안쪽이고
            if grid[r][c] > grid[nr][nc]: # 내리막이라면
                # dfs 호출해서 내 위치에서 갈 수 있는 경로 찾기.
                dp[r][c] += dfs(nr,nc)
    
    return dp[r][c]

dfs(0,0)
print(dp[0][0])