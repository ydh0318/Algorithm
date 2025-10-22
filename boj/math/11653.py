# N = int(input())
# numbers = [True] * (N+1)
# primes = []
# ans = []
# for i in range(2,N+1):
#     if numbers[i]:
#         primes.append(i)
#         for j in range(i,N+1,i):
#             numbers[j] = False
# while N > 1:
#     if N % primes[-1] == 0:
#         ans.append(primes[-1])
#         N = N//primes[-1]
#     else:
#         primes.pop()
# while ans:
#     print(ans.pop())

N = int(input())

i = 2
while i * i <= N:     # √N까지만 확인
    while N % i == 0: # 나누어 떨어지는 동안 계속 나눔
        print(i)
        N //= i
    i += 1

if N > 1:  # 남은 수가 소수라면 출력
    print(N)