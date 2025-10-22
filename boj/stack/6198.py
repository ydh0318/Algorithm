'''
    도시에는 N개의 빌딩이 있다.
    i번째 빌딩의 키가 hi이고 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다.
    i번째 빌딩 관리인이 볼 수 있는 다른 빌딩의 옥상 정원은 i+2, .. , N

    각 관리인이 벤치마킹이 가능한 빌딩의 수의 합을 출력한다.
'''
from collections import deque

N = int(input())
buildings = deque()
for idx in range(N): buildings.append((int(input()), idx))
stack = []
answer = 0

while buildings:
    stack.append(buildings.popleft())
    
    while stack and buildings:
        if stack[-1][0] <= buildings[0][0]: # 보고있는 빌딩이 같거나 높으면
            answer += buildings[0][1] - stack[-1][1] - 1 # 총 보고있는 빌딩 수 추가
            stack.pop()
        else: break

last_height, last_idx = stack.pop()
for i in range(len(stack)):
    if stack[i][0] <= last_height: # 같으면 이전 빌딩까지만 볼 수 있음
        answer += last_idx - stack[i][1] - 1
    else: # 
        answer += last_idx - stack[i][1]

print(answer)