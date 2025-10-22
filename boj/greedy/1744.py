# 수 묶기

'''
    길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 함.
    
    수열의 두 수를 묶어서 구하는데, 어떤 수를 묶으려고 할 때,
    위치에 상관없이 묶을 수 있다.
    
    하지만, 같은 위치(자기 자신)에 있는 수를 묶는 것은 불가능하다.
    
    수를 묶는다는 것은 두 수를 곱하는 것이다.
    
    수열이 주어질 때, 두 수를 묶은 수열의 합이 최대가 되도록 한다.
    단, 수열의 모든 수는 단 한 번만 묶거나, 묶지 않아야한다.
'''

'''
    정렬 후 큰 수 부터 묶음
    음수가 짝수개면 상관없음
    음수가 홀수개면
        0이 있으면 묶고
        0이 없으면 가장 작은 음수를 묶지않음.
    
    양수는 1을 체크
    
'''

N = int(input())
positive = []
negative = []
zero = 0
ans = 0
for i in range(N):
    now = int(input())
    if now < 0:
        negative.append(now)
    elif now == 0:
        zero += 1
    else:
        positive.append(now)

positive.sort()
negative.sort(reverse=True)
# print(positive)
# print(negative)

if len(negative) > 0:
    if len(negative) % 2 != 0: # 홀수개일때
        if zero > 0: # 0이 있으면 가장 작은 수 묶음.
            negative.pop(0)
        else: # 없으면 가장 작은 수만 안 묶음
            ans += negative.pop(0)

while positive:
    if len(positive) > 1:
        a = positive.pop()
        b = positive.pop()
        if a == 1 or b == 1:
            ans += a + b
        else:
            ans += a*b
    else: break
if positive:
    ans += positive[0]


while negative:
    if len(negative) > 1:
        a = negative.pop()
        b = negative.pop()
        ans += a*b
    else: break
if negative:
    ans += negative[0]
    
print(ans)