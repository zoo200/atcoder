l, r = map(int, input().split())

MOD = 2019
# 余りだけ考えると
# 1 = 2020 = 4039
# 2 = 2021 = 4040
# 3 = 2022 = 4041
# なのでl=2020 であれば4038(2020+2019-1)まで考慮すれば良い
r = min(r, l + MOD - 1)

res = MOD - 1
for i in range(l, r):
    for j in range(i + 1, r + 1):
        res = min(res, (i % MOD) * (j % MOD) % MOD)
print(res)


