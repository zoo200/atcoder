import numpy as np
import sys

n = int(input())
m = [[sys.maxsize] * n for _ in range(n) ]
d = {}
vm =  {}

# print(m)

# u → v への距離c を入れる
for i in range(n):
    d[i] = sys.maxsize
    vm[i] = -1

    tmp = list(map(int,input().split()))
    u = tmp[0]
    k = tmp[1]
    for vc in np.array_split(tmp[2:], k):
          m[u][vc[0]] = vc[1]

d[0] = 0

while 1:
    # 一番小さい重みを探す
    minv = sys.maxsize
    u = -1
    for i in range(n):
        if(minv > d[i] and vm[i] != 1):
            u = i
            minv = d[i]

    if(u == -1): break
    vm[u] = 1

    for j in range(n):
        if(vm[j] != 1 and m[u][j] != sys.maxsize):
            if(d[j] > d[u] + m[u][j]):
                d[j] = d[u] + m[u][j]
                vm[j] = 0

for i in range(n):
    print(i,d[i])
    
# in
# 5
# 0 3 2 3 3 1 1 2
# 1 2 0 2 3 4
# 2 3 0 3 3 1 4 1
# 3 4 2 1 0 1 1 4 4 3
# 4 2 2 1 3 3

# out
# 0 0
# 1 2
# 2 2
# 3 1
# 4 3

# map
# --------1
# |       |
# |(2)    |(4)
# |       |
# 0-------3-------4
# |  (1)  |  (3)  |
# |       |       |
# |(3)    |(1)    |(1)
# |       |       |
# --------2--------

