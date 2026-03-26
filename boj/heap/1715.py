# 260326
# G4 카드 정렬하기

'''
    정렬된 두 묶음의 숫자 카드가 있음.
    각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서
    하나로 만드는 데에는 A + B 번의 비교를 해야함.

    매우 많은 숫자 카드 묶음이 책상 위에 놓여 있음.

    이들을 두 묶음씩 골라 합친다면, 고르는 순서에 따라서
    비교 횟수가 달라짐
    1 <= N <= 100,000
'''

'''
    숫자가 작은 것 부터 모아야 함.
'''
import heapq

N = int(input())
numbers = list()
heapq.heapify(numbers)

for _ in range(N):
    heapq.heappush(numbers, int(input()))

ans = 0

if N > 1:
    a1,a2 = 0,0
    while len(numbers) > 1:
        a1 = heapq.heappop(numbers)
        a2 = heapq.heappop(numbers)
        heapq.heappush(numbers, a1+a2)
        ans += a1 + a2
    print(ans)
else:
    print(ans)