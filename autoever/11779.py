# 11779 - 최소비용 구하기 2
# 260404

'''
    n(1<=n<=1,000)개의 도시가 있고, 한 도시에서 출발해서 다른 도시로 출발하는
    m(1<=m<=100,000)개의 버스가 있다.
    우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.

    A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라.
    단, 항상 시작점에서 도착점으로의 경로가 존재함.
'''
import heapq, sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

# 버스의 정보
bus = defaultdict(list)
# 어느 도시에서 온 것인지 기록
prev_node = [0] * (n+1)
# 거리
distance = [float('inf')] * (n+1)

for _ in range(m):
    s, e, w = map(int, input().split())
    bus[s].append((e,w))

heap = []
start_node, end_node = map(int, input().split())

# 시작 노드 초기화
distance[start_node] = 0
heapq.heappush(heap,(start_node,0))
while heap:
    now, dist = heapq.heappop(heap)

    # 현재 거리보다 짧다면 패스
    if distance[now] < dist: continue

    # 갈 수 있는 인접 노드 cost 계산
    for next, weight in bus[now]:
        # 현재 노드 + 다음 노드까지의 거리가 현재 저장되어있는 거리보다 짧다면
        cost = distance[now] + weight
        if cost < distance[next]:
            # 갱신하고 heap에 푸시
            prev_node[next] = now
            distance[next] = cost
            heapq.heappush(heap,(next,cost))

# 2. 수정: 경로 역추적 (가장 깔끔한 방식)
path = []
curr = end_node
while curr != 0: # 시작점의 prev_node가 0이 될 때까지
    path.append(curr)
    curr = prev_node[curr]

path.reverse()
print(distance[end_node])
print(len(path))
print(*path)
# print(prev_node)
# print(distance)