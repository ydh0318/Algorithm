'''
   N개의 로프가 있는데 이런 저런 물체를 들어올릴 수 있다.
   각각의 로프는 그 굵기나 길이가 다르기 때문에 
   들 수 있는 물체의 중량이 서로 다를 수 있다.
   
   여러개의 로프를 병렬로 연결하면 중량을 나눌 수 있다.
   k개의 로프를 사용하면 중량이 w인 물체를 들어올릴 때, 각각의 로프엔
   모두 고르게 w/k 만큼의 중량이 걸리게 된다.
   
   각 로프가 주어질 때, 들어올릴 수 있는 최대 중량을 구하여라
'''

'''
    로프를 내림차순으로 정렬
    0번이 가장 큰 것
    0번 -> ropes[0]
    1번 -> max(ropes[0], ropes[1] * (i+1))
'''

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)
# print(ropes)
max_weight = -1
for i,k in enumerate(ropes):
    if k * (i + 1) >= max_weight:
        max_weight = k * (i + 1)
print(max_weight)