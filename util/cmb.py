n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
 
 
def cmb(n, r, mod):
    r = min(r, n - r)
    x = 1
    y = 1
    for i in range(r):
        x = x * (n - i) % mod
        y = y * (i + 1) % mod
    y = pow(y, mod-2, mod)
    return x * y % mod
 

ans = pow(2, n, mod) - 1 - cmb(n, a, mod) - cmb(n, b, mod)
while ans < 0:
    ans += mod
print(ans)

# https://atcoder.jp/contests/abc156/submissions/10341670
