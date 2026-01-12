# 13414 수강신청

'''
Docstring for 13414
수강신청 버튼이 활성화 된 후, 수강신청 버튼을 조금이라도 빨리 누른 학생이
대기열에 먼저 들어감
1. 이미 대기열에 들어가 있는 상태에서 누르면 맨 뒤로 밀려남
2. 버튼이 비활성화 되면, 가장 앞에 있는 순서대로 신청되며 나머지는 무시함.
'''
from collections import defaultdict
import sys
input = sys.stdin.readline

queue = defaultdict()
K, N = map(int, input().split())
for i in range(N):
    s = input()
    queue[s] = i

ans = list(queue.items())
ans.sort(key=lambda x : x[1])
for i in range(min(K,len(ans))):
    print(ans[i][0],end='')