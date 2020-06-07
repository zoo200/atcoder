mod=10**9+7

d=int(input())
s=input()
n=len(s)

dp=[[[0] * 100 for _ in range(2)] for _ in range(n+1)]
dp[0][0][0]=1

for i in range(n):
    # 全部の余りパターン処理
    now= int(s[i])

    for j in range(d):

        # ここでやったほうが少しだけ早かった
        # （ちなみに何もしないで最後でまとめてやろうとするとTLE
        # case01 666ms → 499 ms, case02 955ms → 674 mx
        # dp[i][1][j] %= mod
        # dp[i][0][j] %= mod

        # smaller 1 -> 全部OK
        for k in range(10):
            dp[i+1][1][(j+k)%d] += dp[i][1][j]
            dp[i+1][1][(j+k)%d]%=mod


        # smaller 0,next smaller 1 -> nowより小さいのを全部
        for k in range(now):
            dp[i+1][1][(j+k)%d] += dp[i][0][j]
            dp[i+1][1][(j+k)%d] %=mod

        # smaller 0,next smaller 0 -> nowだけ
        dp[i+1][0][(j+now) % d] = dp[i][0][j]


#-1 dp[n][1][0]に、0 の時が余分に加えられている
ans=dp[n][0][0] + dp[n][1][0]-1

print(ans%mod)
