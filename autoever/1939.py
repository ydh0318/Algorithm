import sys
from collections import deque
input = sys.stdin.readline

def bfs(mid):
    # mid 무게를 싣고 start_node에서 end_node까지 갈 수 있는지 확인하는 BFS
    q = deque([start_node])
    visited = [False] * (N + 1)
    visited[start_node] = True
    
    while q:
        now = q.popleft()
        
        # 도착지에 도달했다면 이 무게(mid)로 이동 가능한 것이므로 True 반환
        if now == end_node:
            return True
            
        for next_node, weight_limit in graph[now]:
            # TODO 1: 어떤 조건일 때 큐에 다음 노드를 넣어야 할까요?
            # 힌트: 아직 방문하지 않았고, 다리의 하중 제한이 트럭의 무게(mid)보다 크거나 같아야 함
            if not visited[next_node] and weight_limit >= mid:
                visited[next_node] = True
                q.append(next_node)
                
    # 큐가 빌 때까지 도착지에 도달하지 못했다면 이동 불가능
    return False

# ----------------- 입력 및 초기화 -----------------
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_weight = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    max_weight = max(max_weight, C) # 이분 탐색의 최대 범위를 잡기 위해 저장

start_node, end_node = map(int, input().split())

# ----------------- 이분 탐색 로직 -----------------
low = 1
high = max_weight
ans = 0

while low <= high:
    mid = (low + high) // 2
    
    # TODO 2: bfs(mid)의 결과에 따라 low, high, ans를 어떻게 업데이트할까요?
    if bfs(mid):
        # 이동 가능하다면? 무게를 더 늘려보자! (그리고 현재 무게는 정답 후보로 저장)
        ans = mid
        low = mid + 1
    else:
        # 이동 불가능하다면? 무게를 줄여야 함!
        high = mid - 1

print(ans)