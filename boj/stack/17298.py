'''
    수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
    Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에
    있는 수를 의미한다. 그러한 경우가 없는 경우엔 오큰수는 -1이다.
'''
N = int(input())
seq = list(map(int, input().split()))

stack = []
result = []

while seq:
    if stack:
        while stack:
            if seq[-1] >= stack[-1]:
                stack.pop()
            else:
                result.append(stack[-1])
                stack.append(seq.pop())
                break
    else:
        stack.append(seq.pop())
        result.append(-1)
result.reverse()
print(*result)