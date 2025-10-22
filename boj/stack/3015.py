N = int(input())

# 스택에는 [키, 해당 키를 가진 연속된 사람 수]를 저장
stack = []
answer = 0

for _ in range(N):
    h = int(input())
    # 현재 사람(h)보다 키가 작은 사람들은 스택에서 pop
    # 이 사람들은 h를 볼 수 있고, h에 의해 시야가 막힘
    while stack and stack[-1][0] < h:
        answer += stack.pop()[1]
    # 스택이 비어있으면 현재 사람을 추가하고 다음으로 넘어감
    if not stack:
        stack.append([h, 1])
        continue
    # 스택 top의 키가 h와 같다면
    if stack[-1][0] == h:
        # 스택 top의 연속된 사람 수를 가져옴
        cnt = stack.pop()[1]
        answer += cnt
        # 스택에 아직 사람이 남아있다면(가장 가까운 같은 키 그룹 너머에 사람이 있다면),
        # 그 사람들은 h와 같은 키를 가진 사람들 너머로 h를 한 명 더 볼 수 있음
        if stack:
            answer += 1
        # 현재 h를 포함하여 연속된 사람 수를 스택에 다시 push
        stack.append([h, cnt + 1])
    # 스택 top의 키가 h보다 크다면
    else: # stack[-1][0] > h:
        # top의 사람은 h를 볼 수 있음
        answer += 1
        stack.append([h, 1])

print(answer)