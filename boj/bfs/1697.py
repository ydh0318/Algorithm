from collections import deque

N, K = map(int, input().split())

q = deque()
q.append((N,0))

dx = [-1,1,0]

if N > K:
    print(abs(K-N))
else:
    visited = [False] * (2*K+1)
    visited[N] = True
    
    while q:
        curr_pos, curr_time = q.popleft()
        # print(curr_pos, curr_time)
        if curr_pos == K:
            print(curr_time)
            break
        
        for i in range(3):
            new_p = 0
            if dx[i] == 0:
                new_p = curr_pos * 2
            else:
                new_p = curr_pos + dx[i]
            
            if new_p <= 2*K and new_p >= 0:
                if visited[new_p] == False:
                    visited[new_p] = True
                    q.append((new_p,curr_time+1))