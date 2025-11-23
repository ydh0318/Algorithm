while True:
    l = list(map(int, input().split()))
    if sum(l) == 0: break
    l.sort()
    if l[0]+l[1] <= l[2]: print('Invalid'); continue
    cnt = len(set(l))
    
    if cnt == 1: print('Equilateral')
    elif cnt == 2: print('Isosceles')
    elif cnt == 3: print('Scalene')