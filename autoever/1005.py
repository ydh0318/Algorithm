# 1005 - ACM Craft
# 260404

'''
    매 게임시작 시 건물을 짓는 순서가 주어진다.
    또한 건물은 각각 건설을 시작하여 완성이 될 때까지 Delay가 존재한다.

    선행 건물이 다 지어지면 다음 건물을 지을 수 있는데,
    만약 선행 건물이 두 개 이상이면 두 건물이 다 지어져야 다음 건물을 지을 수 있다.

    특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 리턴.
'''

'''
    모든 건물의 건설되는 시간을 dp로 구함.
    진입차수가 0이 되어서 q에 추가할 때 선수건물이 지어지는 시간을 dp에서 참조해서 추가함.
'''
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N, K = map(int, input().split())
    indegree = [0] * (N+1)
    buildings = {}
    # 건물당 건설에 걸리는 시간.
    time = [0] + list(map(int, input().split()))
    dp = [0] * (N+1)
    # 건설 순서 X,Y
    for _ in range(K):
        X, Y = map(int, input().split())
        if buildings.get(X):
            buildings[X] = buildings.get(X) + [Y]
        else:
            buildings[X] = [Y]
        indegree[Y] += 1
    W = int(input())

    def topology_sort():
        # 차수 0인거 q에 넣음.
        # 그담에 돌면서 차수 뺌
        # 반복함.
        q = deque()

        for i in range(1,N+1):
            if indegree[i] == 0: q.append(i); dp[i] = time[i]

        while q:
            now = q.popleft()
            # 현재 지어야 할 건물
            # now에서 나가는 화살표 하나씩 없앰
            for next_node in buildings.get(now,[]):
                indegree[next_node] -= 1
                # 이제 후행건물의 예상시간을 미리 업데이트 한다.
                # 후행건물시간 = 지금선행건물 + 후행건물 vs 다른선행건물 + 후행건물
                dp[next_node] = max(dp[next_node], dp[now] + time[next_node])
                if indegree[next_node] == 0: q.append(next_node)
        return
    
    topology_sort()
    print(dp[W])