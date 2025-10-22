'''
    N명이 한 줄로 서서 기다리고 있다
    두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다
    키가 큰 사람이 없어야 한다.
    
    줄에 서 있는 사람의 키가 주어졌을 때, 서로 볼 수 있는 쌍의 수 리턴
    
    7명 : 2 4 1 2 2 5 1
        (1,2), (2,3), (2,4), (2,5), (2,6)
        (3,4), (4,5), (4,6), (5,6), (6,1)
'''
'''
    나랑 마주볼 수 있는 애들만 남기기
    나와 마주 본다는 것은? 나와 마주보는 사람 사이에 둘 보다 큰 사람이 없어야 함.

    내 직전에 오는것이 크면, 그 이전에 있던것들은 다 못만남.
'''

N = int(input())
answer = 0

'''
    사람들을 반으로 나누어 왼쪽 오른쪽에 집어넣고
    각 그룹에서 max인것을 기록해서 마주보는것을 추가함.
    이분탐색?
    
    1. 스택을 반으로 나눈다.
    2. 원소의 개수가 짝수인 것과 홀수인 것을 나눈다.
'''

def divide_list(seq, start, end):
    # base case: 분할된 부분의 길이가 3 이하이면 재귀를 멈추고 출력
    if end - start < 3:
        find_pair(start,end,seq)
        #print(f"분할 완료 (길이 3 이하): {seq[start:end]}")
        return

    # 중앙 인덱스 계산
    mid = (start + end) // 2
    
    # print(f"분할 중: {seq[start:end]} -> {seq[start:mid]} 와 {seq[mid:end]}")

    # 재귀 호출: 리스트(seq)는 그대로 두고, 인덱스(start, end)만 변경해서 전달
    divide_list(seq, start, mid)
    divide_list(seq, mid, end)
    find_pair(start,end,seq)


def find_pair(start, end, seq):
    global answer

    mid = (start + end) // 2
    prev_max = 0
    left = seq[start:mid]
    right = seq[mid:end]

    # print(left, right)
    right.reverse()
    cnt = 0
    # 왼쪽 오른쪽을 비교하며 계산함
    while left and right:
        # 왼쪽이 오른쪽보다 크고 오른쪽이 이전에 pop했던것보다 크다면
        # 오른쪽을 팝하고 max를 갱신함.
        if left[-1] >= right[-1]:
            if min(right[-1],left[-1]) >= prev_max:
                prev_max = max(prev_max, right[-1])
                right.pop()
                cnt += 1
            else:
                prev_max = max(prev_max, right[-1])
                right.pop()
        elif left[-1] < right[-1]:
            if min(right[-1],left[-1]) >= prev_max:
                prev_max = max(prev_max, left[-1])
                left.pop()
                cnt += 1
            else:
                left.pop()
    # print(cnt)

    answer += cnt
    return

seq = []
for _ in range(N):
    seq.append(int(input()))

divide_list(seq,0,N)
print(answer)