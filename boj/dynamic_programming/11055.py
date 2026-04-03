# 가장 큰 증가하는 부분 수열
# 251127

N = int(input())
seq = list(map(int,input().split()))
# 수열의 합, 해당 수열의 가장 큰 수

# table[i]는 seq[i]를 마지막 숫자로 가지는 수열 중 가장 큰 합.
table = seq[:]

# 2중 포문 사용
for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            table[i] = max(table[i], table[j]+seq[i])

print(max(table))