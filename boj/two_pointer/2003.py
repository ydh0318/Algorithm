# 수들의 합 2

'''
Docstring for 2003
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 
다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 
각각의 A[x]는 30,000을 넘지 않는 자연수이다.

현재 합이 M 보다 같음 -> 정답 +1 하고 p1 도 +1
현재 합이 M 보다 큼 -> p1 + 1
현재 합이 M 보다 작음 -> p2 + 1
'''

N, M = map(int, input().split())
A = list(map(int, input().split()))

p1,p2,prefix_sum,ans = 0,0,A[0],0
while p1 < N and p2 < N:
    if prefix_sum == M:
        # print(p1,p2)
        ans += 1
        prefix_sum -= A[p1]
        p1 += 1
    elif prefix_sum > M: 
        prefix_sum -= A[p1]
        p1 += 1
    elif prefix_sum < M:
        p2 += 1
        if p2 == N:
            break
        prefix_sum += A[p2]

print(ans)