'''
    N개의 회의에 대해 사용표를 만들고자 한다.
    각 회의의 시작시간과 끝나는 시간이 주어지고, 각 회의가 겹치지 않게
    회의실을 사용할 수 있는 회의의 최대 개수를 리턴
    
    회의가 종료되자마자 다음 회의가 시작 될 수 있고, 
    시작시간과 끝나는 시간이 같을수도 있음
'''

N = int(input())
times = [list(map(int,input().split())) for _ in range(N)]
times.sort(key=lambda x : (x[0],x[1]))
print(times)
using = 0
cnt = 0
for start, end in times:
    if start >= using:
        print(using,start,end)
        cnt += 1
        using = end
        
print(cnt)