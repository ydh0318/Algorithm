# 2252 - 줄 세우기
# 260404

'''
    N명의 학생들을 키 순서대로 줄을 세우려고 함.
    근데 전체 학생의 키를 알 방법이 없어서 두 명의 키를 비교해서 계속 세우려고 함.
    그나마도 모든 학생이 아닌 일부 학생들의 키를 비교한 것.
    그 결과가 주어졌을 때, 줄을 세운 결과를 리턴
'''

'''
    위상정렬이란 대학교의 선수과목과 비슷한 맥락
    1. 진입차수(나에게 들어오는 화살표)
        내 순서가 되기 전에 먼저 선행되어야 하는 일의 수
    2. queue를 활용
        모든 노드의 진입차수를 계산하여 배열에 담는다.
        진입 차수가 0인 노드를 모두 queue에 넣는다.
        큐가 빌 때까지 다음의 행동을 반복한다.
            큐에서 진행 가능한 노드를 꺼냄
            그 노드에서 나가는 화살표를 모두 제거
            방금 차수를 줄인 노드 중 0이 된 것이 있다면 새롭게 큐에 넣음.
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def topology_sort():
    result = [] # 수행결과를 담을 리스트
    q = deque()

    # 1. 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1,N+1):
        if indegree[i] == 0: q.append(i)
    
    # 2. 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)

        # 3. 이 노드에서 나가는 차수들 하나씩 지움.
        for next_node in student[now]:
            indegree[next_node] -= 1
            # 지웠을 때 차수가 0이면 다시 큐에 삽입.
            if indegree[next_node] == 0: q.append(next_node)
    
    # 결과 리턴
    return result


# 학생의 수 M, 비교결과 M개, 학생들의 번호는 1~N
N, M = map(int, input().split())
indegree = [0] * (N+1)
student = defaultdict(list)

for _ in range(M):
    # a학생이 b학생보다 앞에 서야한다는 뜻.
    a, b = map(int, input().split())
    # a보다 큰 학생들을 넣음.
    student[a].append(b)
    # b앞에 작은 학생 한 명 추가
    indegree[b] += 1

print(*topology_sort())