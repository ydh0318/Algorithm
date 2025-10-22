'''
    키로거는 사용자가 키보드를 누른 명령을 모두 기록한다.
    따라서 강산이가 비밀번호를 입력시, 화살표나 백스페이스를 입력해도 알아낼 수 있다
    알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표를 눌렀을 때 비밀번호를 알아내자
'''
from collections import deque

tc = int(input())

for _ in range(tc):
    code = list(input())
    passs = deque()
    word = deque()
    for c in code:
        if c == '<':
            if passs: word.appendleft(passs.pop())
        elif c == '>':
            if word: passs.append(word.popleft())
        elif c == '-':
            if passs: passs.pop()
        else:
            passs.append(c)
    
    print(''.join(passs) + ''.join(word))