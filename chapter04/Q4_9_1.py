N = int(input())
d = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(N - 1):
        if d[j] < d[j + 1]:
            d[j], d[j + 1] = d[j + 1], d[j]

print(*d)
