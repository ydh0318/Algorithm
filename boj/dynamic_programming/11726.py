'''
    2x1 -> 1
    2x2 -> 
    2x3 -> 이전이전거 + 2칸 , 이전거 + 1칸
    2x4 -> 4
    2x5 -> 
'''
n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[-1] % 10007)