'''
    2N 개의 길 중 지나갈 수 있는 길의 개수를 구하시오
    
    경사로를 놓으려면.
        1. 낮은 칸에 놓으면, L개의 연속된 칸에 바닥이 모두 접해야 함.
        2. 낮은 칸과 높은 칸의 차이는 1이어야 함.
        3. 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 함.
    놓을 수 없는 경우
        1. 놓은곳에 또 놓이는 경우.
        2. 범위를 벗어나는 경우
        
    경사로 확인 로직
    현재 위치와 다음 위치의 높이 차를 확인함
    만약 차이가 없으면 다음 위치 확인
    만약 차이가 있으면
    내가 다음거보다 높을 때와 내가 다음거보다 낮을 때를 분기
        2 이상일시 fail
        1 이면 현재위치에서 L 떨어진 위치 까지 확인해야 함.
            높이가 다르거나, 범위를 벗어나거나, 이미 경사로가 놓여있으면?   
            -> fail
'''

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for row in grid:
    if len(set(row)) == 1: 
        ans += 1
    else: 
        gyengsa = [False] * N
        possible = True
        
        for i in range(N-1):
            diff = row[i] - row[i+1]
            # 만약 차이가 없으면 다음 위치 확인
            if not possible: break # 해당 row는 불가능함
            if diff == 0: continue
            # 다음 위치가 현재 위치보다 낮은 경우
            elif diff == 1 and i + L < N:
                # 1 이면 현재위치에서 L 떨어진 위치까지 확인해야 함.
                for j in range(i+1,i+L+1):
                    # 높이가 다르거나 이미 경사로가 놓여있으면? 
                    if gyengsa[j] or row[i] - row[j] != 1:
                        # print('내리막 분기',row,row[i],row[j])
                        possible = False
                        break
                # 경사로 놓음 표시
                if possible:
                    for j in range(i+1,i+L+1):
                        gyengsa[j] = True
                    
            # 다음 위치가 현재 위치보다 높은 경우
            elif diff == -1 and i + 1 - L >= 0:
                for j in range(i,i-L,-1):
                    if gyengsa[j] or row[i+1] - row[j] != 1:
                        # print('오르막 분기',row, row[i+1],row[j])
                        possible = False
                        break
                if possible:
                    for j in range(i,i-L,-1):
                        gyengsa[j] = True
            else: # 차이가 2 이상이거나, 범위를 벗어나면 fail
                # print('else 분기', row)
                possible = False
                break
        if possible:
            # print('가능 분기', row)
            ans += 1
            
# print(ans)
# print('열 확인')
for row in list(zip(*grid)):
    if len(set(row)) == 1: 
        ans += 1
    else: 
        gyengsa = [False] * N
        possible = True
        
        for i in range(N-1):
            diff = row[i] - row[i+1]
            # 만약 차이가 없으면 다음 위치 확인
            if not possible: break # 해당 row는 불가능함
            if diff == 0: continue
            # 다음 위치가 현재 위치보다 낮은 경우
            elif diff == 1 and i + L < N:
                # 1 이면 현재위치에서 L 떨어진 위치까지 확인해야 함.
                for j in range(i+1,i+L+1):
                    # 높이가 다르거나 이미 경사로가 놓여있으면? 
                    if gyengsa[j] or row[i] - row[j] != 1:
                        # print('내리막 분기',row,row[i],row[j])
                        possible = False
                        break
                # 경사로 놓음 표시
                if possible:
                    for j in range(i+1,i+L+1):
                        gyengsa[j] = True
                    
            # 다음 위치가 현재 위치보다 높은 경우
            elif diff == -1 and i + 1 - L >= 0:
                for j in range(i,i-L,-1):
                    if gyengsa[j] or row[i+1] - row[j] != 1:
                        # print('오르막 분기',row, row[i+1],row[j])
                        possible = False
                        break
                if possible:
                    for j in range(i,i-L,-1):
                        gyengsa[j] = True
            else: # 차이가 2 이상이거나, 범위를 벗어나면 fail
                # print('else 분기', row)
                possible = False
                break
        if possible:
            # print('가능 분기', row)
            ans += 1

print(ans)