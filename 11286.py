# 260327

# S1 절댓값 힙

'''
    배열에 정수x(x != 0)를 넣는다.
    절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
    절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고,
    그 값을 배열에서 제거한다.
'''
import heapq, sys

sys.stdin.readlines = input

N = int(input())
heap = list()
heapq.heapify(heap)
for _ in range(N):
    ip = int(input())
    if ip != 0: heapq.heappush(heap,(abs(ip),ip))
    else:
        if heap: _, a = heapq.heappop(heap); print(a)
        else: print(0)
