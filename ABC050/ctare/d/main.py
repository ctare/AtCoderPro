#! cat input | python3 main.py
n = int(input())


s = str(n)
dp = [[0 for x in range(2)] for x in range(len(s) + 1)]
dp[0][0] = 1
for i in range(len(s)):
    for j in range(2):
        limit = 9 if j else int(s[i])
        for d in range(limit + 1):
            dp[i + 1][j or d < limit] += dp[i][j]
print(dp)


# # 0 0 : 1 => (0 0, )
# # 1 0 : 0 => (, )
# # 1 1 : 0 => (, )
#
# # a + b <= s
# # a ^ b <= x
# # b in a
#
# # 0 0
# # 2a' + 2b' <= s
# # 2a' ^ 2b' <= x
# # 2b' in 2a'
# #
# # a' + b' <= s // 2
# # a' ^ b' <= x // 2
# # b' in a'
#
# # 1 0
# # (2a' + 1) + 2b' <= s
# # (2a' + 1) ^ 2b' <= x
# # 2b' in (2a' ^ 1)
# #
# # a' + b' <= (s - 1) // 2
# # a' ^ b' <= (x - 1) // 2
#
# # 1 1
# # (2a' + 1) + (2b' + 1) <= s
# # (2a' + 1) ^ (2b' + 1) <= x
# # a' + b' <= (s - 2) // 2
# # a' ^ b' <= s // 2     1 ^ 1 == 0
#
# def solve(s, x):
#     if x <= 1 and s <= 1:
#         if x == s:
#             return 1
#         else:
#             return 0
#
#     return (
#             solve(s // 2, x // 2) + # 0 0
#             solve((s - 1) // 2, (x - 1) // 2) + # 1 0
#             solve((s - 2) // 2, x // 2)
#             )
#
# print(solve(0, 2))
#
# 11010 10111
# 01000 10000
#
