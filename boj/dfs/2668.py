'''
   가로로 N개의 칸
   첫째 줄에서 숫자를 적절히 뽑고,
   뽑힌 정수들이 이루는 집합과, 바로 밑의 둘째 줄에 들어어있는
   정수들의 집합이 일치함.

   최대한 많이 위의 조건을 만족시키는 정수들을 뽑으시오 
'''
from collections import defaultdict

graph=defaultdict(list)

N=int(input())
arr=list()
ans=list()

for _ in range(N):
    arr.append(int(input()))

for idx, num in enumerate(arr):
    graph[idx+1].append(num)

# cycle 찾기
# 탐색 수행
def find_cycle(node):
    '''
        깊이우선탐색으로 사이클 확인한 후 ans에 추가
    '''
    stack = [node]
    visited = set()
    while stack:
        curr = stack.pop()
        for v in graph[curr]:
            if v not in visited:
                visited.add(v)
                stack.append(v)

    return True if node in visited else False
            
for i in range(1,N+1):
    if find_cycle(i):
        ans.append(i)

print(len(ans))
ans.sort()
for v in ans: print(v)