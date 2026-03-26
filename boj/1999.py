# 260224-G3

'''
    N x N의 행렬이 있음.
    0~249의 숫자
    K개의 질문이 주어질 때, 각 질문은 주어진 행렬의 B x B 크기의
    부분 행렬의 최댓값과 최솟값의 차이를 묻는 질문임.
    각 질문에 대해 부분 행렬의 가장 왼쪽 위의 위치가 주어지며,
    모든 값은 같은 B값을 갖는다.
'''
'''
    DP
    
'''

N,B,K = map(int, input().split())

mat = list()
for _ in range(N):
    mat.append(list(map(int, input().split())))

dp = [[0]*(N) for _ in range(N)]

# 누적합 구하기
# dp[0][0]=mat[0][0]
# for i in range(1,N):
#     dp[0][i] = dp[0][i-1] + mat[0][i]
# for i in range(1,N):
#     dp[i][0] = dp[i-1][0] + mat[i][0]
# for i in range(1,N):
#     for j in range(1,N):
#         dp[i][j] = dp[i-1][j] + dp[i][j-1] + mat[i][j] - dp[i-1][j-1]

# N,N의 위치부터 BxB 크기 안에 속한 최댓값 최솟값을 기록해놓은
# 행렬을 두개 기록함.

# 누적합 확인
for m in dp: print(m)



# dp table 순회
for _ in range(K):
    i,j = map(int, input().split())

