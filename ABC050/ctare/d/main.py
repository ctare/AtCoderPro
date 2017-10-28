#! cat input | python3 main.py
n = int(input())

uvs = []
for i in range(n + 1):
    for j in range(n + 1):
        if i ^ j <= n and i + j <= n and i >= j:
            uv = (i^j, i+j)
            if uv not in uvs:
                uvs.append(uv)
                print(uv, i, j)
            # else:
            #     print(uv, i, j)

for u, v in sorted(uvs, key=lambda x: x):
    print(u, v)
