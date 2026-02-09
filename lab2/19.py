n = int(input())
cnt = {}

for _ in range(n):
    name, k = input().split()
    k = int(k)
    cnt[name] = cnt.get(name, 0) + k

for name in sorted(cnt):
    print(name, cnt[name])
