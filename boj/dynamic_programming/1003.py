'''
    0과 1은 n == 2 일 때,
    1은 n == 3 일 때 호출됨.
    
    2는 n이 3,4 일 때 호출 됨.
    3은 n이 4,5 일 떄 호출 됨.
    
    만약 fibo(5)를 호출하면
    1. fibo(4), fibo(3)
    2. fibo(2,3), fibo(1,2)
    3. fobi(0,1,1,2), fibo(0,1)
    
    dp[0]은 fibo(0)호출시 0과 1이 호출되는 횟수 저장
    dp[0][0] = 1 , dp[0][1] = 1
'''

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
length = max(nums)
dp = [[0] * 2 for _ in range(length + 1)]
dp[0][0] = 1
if length > 0:
    dp[1][1] = 1
for i in range(2,length+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for num in nums:
    print(dp[num][0], dp[num][1])