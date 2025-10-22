n = int(input())
giggle = {}

for _ in range(n):
    name, state = input().split()
    giggle[name] = state

enter = []
for n, st in giggle.items():
    if st == 'enter':
        enter.append(n)

enter.sort(reverse=True)
for name in enter:
    print(name)