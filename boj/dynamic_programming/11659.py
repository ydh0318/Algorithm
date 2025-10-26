# 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

# print(numbers)
prefix = [0] * (N+1)
for i in range(1,N+1):
    prefix[i] = prefix[i-1] + numbers[i-1]
    
# print(prefix)

for _ in range(M):
    start, end = map(int, input().split())
    print(prefix[end]-prefix[start-1])
    