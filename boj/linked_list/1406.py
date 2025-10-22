'''
    커서는 문장의 맨 앞, 문장의 맨 뒤, 문장 중간 임의의 곳에 위치할 수 있다.
    길이가 L인 문자열이 있다면, 커서가 위치할 수 있는 공간은 L+1의 공간
    
    초기에 편집기에 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어질 때,
    모든 명령을 수행 후 입력되어 있는 문자열을 구하시오.
    최초에 커서는 문장의 맨 뒤에 위치함.
'''
from collections import deque

left_string = deque(input())
right_string = deque()
N = int(input())

for i in range(N):
    op = input()
    if len(op) != 1:
        _, char = op.split()
        left_string.append(char)
    else:
        if op == 'L': 
            if left_string: right_string.appendleft(left_string.pop())
        elif op == 'D':
            if right_string: left_string.append(right_string.popleft())
        elif op == 'B': 
            if left_string: left_string.pop()
            
print(''.join(left_string) + ''.join(right_string))