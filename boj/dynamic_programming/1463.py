'''
    3으로 나누어 떨어지면, 3으로 나눈다.
    2로 나누어 떨어지면, 2로 나눈다.
    1을 뺀다
    위의 세가지 연산을 할 수 있다.
    
    정수 N이 주어졌을 때, 1을 만들때 사용하는 연산 횟수의 최솟값
'''

'''
    10 -> 1을 만드는 과정
    dp[10][1] -> 10을 만드는 방법은 20//2 or 30//3 or 11-1
    
    역순
    1 -> 10을 만드는 과정
    dp[10] -> 5 * 2 or 9 + 1중 최소값
    min(dp[5] or dp[9]) -> dp[9]
    dp[9] -> 3 * 3 or 8 + 1
    
    tabulation
    dp[1] = 1
    dp[2] = 2//2 + 1 or 1 + 1
'''
N = int(input())
dp = [0] * (N + 1)

for i in range(2,N+1):
    if i%2 == 0 and i%3 == 0:
        dp[i] = min(dp[i//2], dp[i//3], dp[i-1]) + 1
    elif i%3 == 0:
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    elif i%2 == 0:
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])