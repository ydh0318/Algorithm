N, M = map(int, input().split())

str_set = dict()

for _ in range(N):
    s = input()
    str_set[s] = str_set.get(s,0) + 1

cnt = 0

for _ in range(M):
    s = input()
    if str_set.get(s,0) > 0:
        cnt += 1

print(cnt)