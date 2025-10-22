'''
    N개의 높이가 서로 다른 탑을
    수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고, 
    각 탑의 꼭대기에 레이저 송신기를 설치하였다.
    모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수직 직선의 왼쪽으로 발사하고,
    탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다.
    하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다.

    팝하고 역순으로 타워 돌아서 만나는 것에 저장함.
    
    오십만 + 사십구만구천구백구십구 + ... + 1은? = 124,999,975,000
    
    만날때까지 계속 팝
'''
N = int(input())

towers = list(map(int, input().split()))
stack = []
laser_number = [0] * N
cnt = N-1

while len(towers) > 1:
    stack.append((towers.pop(), cnt))
    cnt -= 1
    
    while stack:
        if stack[-1][0] <= towers[-1]: # 현재 기준 왼쪽에 있는 타워에 닿는다면?
            top, idx = stack.pop()
            laser_number[idx] = cnt + 1
        else: break

print(*laser_number)