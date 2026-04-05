from collections import defaultdict
import heapq, sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

graph = defaultdict(list)
V, E = map(int, input().split())
parent = list(x for x in range(V+1))
rank = [0] * (V+1)
mst = []

# union find를 이용해서 트리 최소 가중치 트리 생성함.
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y):
    # 부모가 다르면 다른트리 -> union
    px = find_parent(x)
    py = find_parent(y)
    if px != py:
        # 랭크가 높은 노드에 합침
        if rank[px] > rank[py]:
            parent[py] = px
        elif rank[px] < rank[py]:
            parent[px] = py
        else: # 같으면 아무데나 붙이고 rank + 1
            parent[py] = px
            rank[px] += 1
        return True
    else:
        return False
            

edges = []
for _ in range(E):
    s,e,w = map(int, input().split())
    heapq.heappush(edges, (w,s,e)) # 최소힙에 가중치순으로 정렬
    graph[s].append((w,e))
    graph[e].append((w,s))

# print(graph)
ans = 0
while edges:
    w,s,e = heapq.heappop(edges)
    # 작은 가중치 순으로 mst에 넣음
    if union(s,e):
        mst.append([w,s,e])
        ans += w

print(ans)