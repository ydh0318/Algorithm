T = int(input())
from collections import deque

for _ in range(T):
    p = input()
    n = int(input()) # 배열에 들어있는 숫자 개수
    seq = input().replace('[','').replace(']','').split(',')
    seq = deque(seq)
    
    if seq[0] == '':
        seq.popleft()
        
    reverse_count = 0
    flag = True
    for op in p:
        if op == 'R':
            reverse_count += 1
        elif op == 'D':
            if seq:
                if reverse_count % 2 == 1: # 뒤집힌 상태
                    seq.pop()
                else: # 원 상태로 돌아옴
                    seq.popleft()
            else:
                flag = False
                print('error')
                break
    if reverse_count %2 == 1:
        seq.reverse()
    
    if flag:
        print(str(list(seq)).replace(' ','').replace('\'',''))