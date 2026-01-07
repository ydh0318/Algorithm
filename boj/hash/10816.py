# 숫자 카드 2

'''
Docstring for 10816
상근이는 정수 하나가 적혀있는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수 가 적혀있는 숫자 카드를 몇 개 가지고 있는지

최대 오십만개의 카드 개수
1초
정렬이 되어 있지 않음.
O(N) -> 오십만개
O(N*M) -> 불가능.
'''
from collections import defaultdict

d = dict()
N = int(input())
cards = list(map(int, input().split()))
cards.sort()
for c in cards:
    d[c] = d.get(c,0) + 1

M = int(input())
numbers = list(map(int, input().split()))
ans = []

keys = d.keys()
for target in numbers:
    if target in keys: ans.append(d.get(target))
    else: ans.append(0)

print(*ans)