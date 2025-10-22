'''
    고정된 수열 B에 수열 A의 원소들을 재배열해서
    sigma(A[i]*B[i])의 최솟값을 리턴
'''

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
ans = 0
for i in range(N):
    ans += A[i]*B[i]
print(ans)