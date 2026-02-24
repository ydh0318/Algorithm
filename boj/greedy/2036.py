import sys
input = sys.stdin.readline

N = int(input())
plus=[]
minus=[]
ans=0 
for _ in range(N):
    num = int(input())
    if num == 1: ans+=num
    elif num <= 0: minus.append(num)
    else: plus.append(num)

plus.sort(reverse=True)
minus.sort()

for i in range(0,len(plus),2):
    if i + 1 < len(plus):
        ans += plus[i]*plus[i+1]
    else:
        ans += plus[i]


for i in range(0,len(minus),2):
    if i + 1 < len(minus):
        ans += minus[i]*minus[i+1]
    else:
        ans += minus[i]

print(ans)