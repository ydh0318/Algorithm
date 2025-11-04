string = input()
alphabet = dict()
for ch in string:
    ch = ch.upper()
    alphabet[ch] = alphabet.get(ch,0) + 1

maxcnt = 0
ans = []
for key, cnt in alphabet.items():
    if cnt > maxcnt:
        ans.clear()
        maxcnt = cnt
        ans.append(key)
    elif cnt == maxcnt:
        ans.append(key)

if len(ans) > 1:
    print('?')
else:
    print(ans[0])