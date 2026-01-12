# 걸그룹 마스터 준석이

'''
Docstring for 16165
입력 받을 걸그룹의 수(N), 맞혀야 할 문제의 수를 입력 받는다.

'''
from collections import defaultdict
gg = defaultdict(list)

N, M = map(int, input().split())

for i in range(N):
    gname = input()
    cnt = int(input())
    for _ in range(cnt):
        gg[gname].append(input())

for j in range(M):
    name = input()
    t = int(input())
    if t == 0: # 그룹 이름 주어짐
        for gname in gg.keys():
            if name == gname:
                arr = gg[gname]
                arr.sort()
                print(*arr, sep='\n')
                break
    else: # 멤버 이름 주어짐
        for gname in gg.keys():
            if name in gg[gname]:
                print(gname)
                break