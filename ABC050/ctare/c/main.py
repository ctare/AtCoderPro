#! cat input | python3 main.py
import sys

n = int(input())
a = list(sorted(map(int, input().split())))
M = 10**9 + 7

end = lambda x: print(x) or sys.exit()
result = 1
n2 = n % 2
if n2 == a[0] % 2:
    end(0)
tmp = None
if n2:
    if a[0]:
        end(0)
else:
    if not a[0] == a[1] == 1:
        end(0)
for a1, a2 in zip(a[n2::2], a[n2 + 1::2]):
    if a1 - a2:
        end(0)
    if tmp:
        if a1 - tmp - 2:
            end(0)

    tmp = a1
    result *= 2
    if result >= M:
        result %= M
end(result)
