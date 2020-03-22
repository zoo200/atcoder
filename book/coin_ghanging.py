import sys

n,m = map(int,input().split())

# 硬貨の配列
c = [int(i) for i in input().split()[:m]]

# その金額払うまでの最小枚数
t = {}

for i in range(n+1):
    t[i] = sys.maxsize

t[0] =0

for i in range(m):
    for j in range(n+1):

        # print(i,j)
        # print(t)

        if(j+c[i] >n):
            break

        # print(j+ c[i],t[j+ c[i]], t[j]+1)
        t[j + c[i]] = min(t[j+ c[i]], t[j]+1)

print(t[n])

# p.412
#
# in
# 15 6
# 1 2 7 8 12 50
#
# out
# 2
