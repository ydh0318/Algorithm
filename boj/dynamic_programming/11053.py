# 가장 긴 증가하는 부분 수열
# 251125

N = int(input())

dp = [0]
seq = list(map(int,input().split()))

# 길이가 K인 최장증가 수열 중 끝 값이 가장 작은 것을 저장해 놓으면
# 연장 판단이 가능함.
'''
    dp[i] -> 길이가 i인 최장 증가 수열 중 끝 값이 가장 작은 것을 저장해 놓은 배열
'''
for s in seq:
    if s > dp[-1]:
        dp.append(s)
    elif s < dp[-1]:
        # 들어갈 수 있는 부분을 찾음
        for i in range(len(dp)):
            if s <= dp[i]:
                dp[i] = s
                break
    
print(len(dp)-1)