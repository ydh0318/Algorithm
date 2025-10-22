'''
    N개의 종류의 동전을 가지고 있는데
    동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 함
    
    이때 필요한 동전 개수의 최솟값을 구하는 프로그램
'''
N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

coins.reverse()
cnt = 0
for coin in coins:
    if K == 0: break
    while coin <= K:
        K -= coin
        cnt += 1
        # print(K, coin)
        
print(cnt)