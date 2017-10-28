#! cat input | python3 main.py
n = int(input())
ts = list(map(int, input().split()))
m = int(input())
pxs = [list(map(int, input().split())) for x in range(m)]

all_sum = sum(ts)
for p, x in pxs:
    print(all_sum + (x - ts[p - 1]))
