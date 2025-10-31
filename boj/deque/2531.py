# 25.10.30-13:50
'''
    벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다.
    
    1. 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우
    할인된 정액 가격으로 제공한다.
    
    2. 초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우,
    이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공함.
    만약, 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우,
    요리사가 새로 만들어 손님에게 제공한다.
'''

'''
    손님이 먹을 수 있는 초밥 가짓수의 최댓값을 구함.
    
    만약 K = 4이고, 30번 쿠폰을 받으면,
    30번을 제외하고 연속된 4개의 초밥 중 중복이 아닌 것을 고르면 됨.
    
    어찌 됐건 최대 K + 1개만 먹을 수 있음.
    그렇다면 ?
'''

from collections import deque
# 접시의수, 초밥의 가짓 수, 연속해서 먹는 접시의 수, 쿠폰 번호
N,d,k,c = map(int, input().split())
chobaps = deque()
first_idx = 0

for i in range(N):
    cho = int(input())
    chobaps.append(cho)
    if cho == c and first_idx == 0:
        first_idx = i
# print(chobaps)
idx = first_idx
# print(first_idx)
max_cnt = 0
eaten = deque()

while True:
    
    # print(eaten, chobaps[idx])
    eaten.append(chobaps[idx])
    # print(idx)
    if len(eaten) == k: # k개 먹었으면 확인
        if c not in eaten:
            max_cnt = max(max_cnt, len(set(eaten)) + 1)
        else:
            max_cnt = max(max_cnt, len(set(eaten)))
        eaten.popleft()

    idx = (idx+1) % N
    if idx == first_idx: break # 종료조건
    
cnt = 0
while cnt <= k-2:
    # print(eaten, chobaps[idx])
    eaten.append(chobaps[idx])
    # print(idx)
    if len(eaten) == k: # k개 먹었으면 확인
        if c not in eaten:
            max_cnt = max(max_cnt, len(set(eaten)) + 1)
        else:
            max_cnt = max(max_cnt, len(set(eaten)))
        eaten.popleft()

    idx = (idx+1) % N
    cnt += 1
    
print(max_cnt)
    