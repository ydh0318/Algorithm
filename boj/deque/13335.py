'''
    n개의 트럭이 건너감.
    트럭의 순서는 바꿀 수 없고, 무게는 다를 수 있음.
    
    다리 위엔 최대 w(다리의 길이)대의 트럭만 올라갈 수 있다.
    다리는 최대 L의 무게까지 버틸 수 있다.
    
    모든 트럭이 다리를 건너는 최단시간을 출력
'''
'''
    현재 다리위에 있는 트럭의 개수와 무게를 고려해야 함.
    for 트럭 in 트럭스
    만약 다리위에 있는 무게와 트럭의 무게를 합한것이 L보다 작고,
    현재 다리위에 있는 트럭의 개수가 w-1보다 작거나 같으면
        올라갈 수 있음
'''
from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = deque([0]*w)
cnt, total = 0,0
ans = 0
while trucks:
    if bridge[0] != 0:
        total -= bridge[0]
        cnt -= 1
    bridge.popleft()
    # 다음 트럭 올라갈 수 있는 경우
    if cnt < w and total + trucks[0] <= L:
        cnt += 1
        total += trucks[0]
        bridge.append(trucks.pop(0))
    else:
        bridge.append(0)
    ans += 1

print(ans + w)