p=1000000007
n,m=map(int,input().split())

# 0段目
dp=[1] * (n +1)

for i in range(m):
    a= int(input())
    dp[a] = 0

for i in range(n-2,-1,-1):
    if dp[i] == 0:
        continue

    dp[i] = (dp[i+1] + dp[i+2]) %p

print(dp[0])
