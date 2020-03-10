s=list('ABCDEFG')
t=list('BCDGK')

n = len(s)
m = len(t)

dp = [[0]*(m+1) for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i -1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

def disp(x,y):
    z = dp[x][y]

    if dp[x][y] == 0:
        return
    
    if dp[x-1][y] != z and dp[x][y-1] != z:
        disp(x-1,y-1)
        # print(dp[x][y])
        print(s[x-1])

    if dp[x-1][y] == z:
        disp(x-1,y)
    if dp[x][y-1] == z:
        disp(x,y-1)

[print(i) for i in dp ]

disp(n,m)
