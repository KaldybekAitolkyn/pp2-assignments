#strings бырыншы кездескеннын позициясы
n = int(input())
a = [input() for _ in range(n)]

pos = {}
for i in range(n):
    if a[i] not in pos:
        pos[a[i]] = i + 1

for s in sorted(pos):
    print(s, pos[s])
