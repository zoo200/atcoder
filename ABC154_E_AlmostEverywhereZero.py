s = input()
K = int(input())
n =len(s)

# dp[i][j][k]
# -> i桁目、j個の非0の数、k 0:そこまでの桁はnと一緒。1:そこまでの桁でn以下であることが確定
# 以下な感じの3次元配列
# [[1, 0], [0, 0], [0, 0], [0, 0]]
# [[0, 1], [1, 0], [0, 0], [0, 0]]
# [[0, 1], [1, 9], [0, 0], [0, 0]]
dp = [[[0] * 2 for _ in range(4)] for _ in range(101)]

dp[0][0][0]=1
for i in range(n):
    for j in range(4):
        for k in range(2):
            nd = int(s[i])

            for d in range(10):
                ni = i+1; nj = j; nk = k

                if d != 0 :nj+=1
                if nj > K:continue
                if k==0:
                    if d > nd:continue
                    if d < nd:nk =1
                dp[ni][nj][nk] += dp[i][j][k]
                # print(d,k)
                # print(i,j,k,dp[i][j][k])
                # print(ni,nj,nk,dp[ni][nj][nk])
                # [print(i) for i in dp]

ans=dp[n][K][0] + dp[n][K][1]
print(ans)
# [print(i) for i in dp]
