# G4-18430 무기공학

'''
    재료의 부위마다 그 강도가 조금 다름
    넓은 사각형 형태의 나무 재료를 잘라 여러 개의 부메랑을 만들어야 함.
    부메랑은 항상 3칸을 차지하는 ㄱ모양이며 4가지의 형태로 제작 가능하다.

    이 때, 부메랑의 중심이 되는 칸은 강도의 영향을 2배로 받음.
    
    만들 수 있는 경우의 수 중 강도 합의 최댓값을 출력하시오.
    (1 ≤ N, M ≤ 5)
'''
# 각 케이스 별
# 좌우 조건
c1 = [(0,-1),(0,-1),(0,1),(0,1)]
# 위아래 조건
c2 = [(1,0),(-1,0),(-1,0),(1,0)]
ans=0

def find_best_strength(idx,visited,now_st):
    global ans
    '''
        최대 25칸 -> 완탐
        모서리를 기준으로 4개를 만들 수 있음.

        모든 칸을 시작 모서리로 돌려서 구함
        4개의 부메랑 형태를 조건으로 달아서
        가능하면 만들고 백트래킹 해서 다음 조건을 넘어감.
        
        안 만들고 넘기기,
        만들고 넘기기(4가지 선택)
    '''
    # 다 돌면 강도 비교하고 끝.
    if idx == N*M:
        ans = max(ans,now_st)
        return

    row, col = idx//M, idx%M
    
    if visited[row][col]:
        # 이미 부메랑이 만들어 진 곳.
        find_best_strength(idx+1, visited, now_st)
    else:
        # 부메랑 안 만들고 넘어감.
        find_best_strength(idx+1, visited, now_st)
        # 조건 네가지 경우 고려함.
        for i in range(4):
           # 만약 부메랑 만들 수 있으면 만들고 넘어감
           new1 = (row+c1[i][0],col+c1[i][1])
           new2 = (row+c2[i][0],col+c2[i][1])
           # 세 칸이 전부 범위 안이고, 칸이 비어 있으면 만듦.
           if 0 <= row < N and 0 <= col < M and not visited[row][col]:
               if 0 <= new1[0] < N and 0 <= new1[1] < M and not visited[new1[0]][new1[1]]:
                   if 0 <= new2[0] < N and 0 <= new2[1] < M and not visited[new2[0]][new2[1]]:
                       visited[row][col] = True
                       visited[new1[0]][new1[1]] = True
                       visited[new2[0]][new2[1]] = True
                       find_best_strength(idx+1, visited, now_st+(strength[row][col]*2)+strength[new1[0]][new1[1]]+strength[new2[0]][new2[1]])
                       # 백트래킹 수행
                       visited[row][col] = False
                       visited[new1[0]][new1[1]] = False
                       visited[new2[0]][new2[1]] = False

N, M = map(int, input().split()) # N 세로, M 가로
strength = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

find_best_strength(0,visited,0)
print(ans)