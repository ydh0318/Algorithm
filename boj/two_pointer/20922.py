import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int,input().split()))
ans = 0
table = [0] * (max(arr)+1)
pointer = 0
for i in range(N):
    table[arr[i]] += 1
    
    if table[arr[i]] > K:
        while table[arr[i]] > K:
            table[arr[pointer]] -= 1
            pointer += 1
    ans = max(ans, i-pointer+1)

print(ans)