'''
    N명의 사람들이 줄을 서 있다.
    i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
    
    사람들이 줄을 서는 순서에 따라 전체 인출 시간의 합이 달라진다.
'''

N = int(input())
times = list(map(int, input().split()))
times.sort()
ans = 0
total = 0
for t in times:
    total += t
    ans += total
print(ans)