n = int(input())
dy = [-1,1,0,0]
dx = [0,0,-1,1]
import copy
from collections import deque

grid = list(list(map(int, input().split())) for _ in range(n))
min_value = 100
max_value = 0
for i in range(n):
        for j in range(n):
            if grid[i][j] < min_value: 
                min_value = grid[i][j]
            if grid[i][j] > max_value:
                max_value = grid[i][j]
            
answer = 1   
for level in range(min_value, max_value):
    cnt = 0
    temp = copy.deepcopy(grid)
    # visited = [[False] * n for _ in range(n)]
    
    start_pos = deque()
    for i in range(n):
        for j in range(n):
            if temp[i][j] <= level:
                temp[i][j] = -1
            else:
                start_pos.append((i,j))
                
    # for row in temp:
    #     print(row)
    # print()
    def bfs(y,x):
        global cnt
        
        if temp[y][x] == -1:
            return
        queue = deque()
        queue.append((y,x))
        while queue:
            row, col = queue.popleft()
            for i in range(4):
                n_row, n_col = row + dy[i], col + dx[i]
                if 0 <= n_row < n and 0 <= n_col < n:
                    if temp[n_row][n_col] != -1:
                        temp[n_row][n_col] = -1
                        queue.append((n_row, n_col))
        cnt += 1
        return
    
    for row, col in start_pos:
        bfs(row,col)
    
    answer = max(answer, cnt)

print(answer)