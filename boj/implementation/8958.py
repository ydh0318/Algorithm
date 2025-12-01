for _ in range(int(input())):
    arr = list(input())
    ans,cnt = 0,0
    for a in arr:
        if a == 'O': cnt += 1; ans += cnt
        else: cnt = 0
    print(ans)