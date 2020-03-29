from collections import defaultdict
import sys

v,e = map(int,input().split())
d = defaultdict(dict)
m = sys.maxsize

# 頂点i→j のkv初期化
for i in range(v):
    for j in range(v):
        d[i][j] = 0 if (i ==j ) else m

for _ in range(e):
    a,b,c = map(int,input().split())
    d[a][b] = c

for k in range(v):
    for i in range(v):
        if(d[i][k] == m): continue
        
        for j in range(v):
            if(d[k][j] == m): continue
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])

for i in range(v): 
    if(d[i][i]) < 0 :
        print('Negarive Cycle')
        exit()

for i in range(v):
    for j in range(v):
        if(d[i][j] == m):
            print("z",end="")
        else:
            print(d[i][j],end="" )
        print(" ",end="")
    print("")

# p 336
# in
# 4 6
# 0 1 1
# 0 2 5
# 1 2 2
# 1 3 4
# 2 3 1
# 3 2 7
# out
# 0 1 3 4 
# z 0 2 3 
# z z 0 1 

# in
# 4 6
# 0 1 1
# 0 2 -5
# 1 2 2
# 1 3 4
# 2 3 1
# 3 2 7
# out
# 0 1 -5 -4 
# z 0 2 3 
# z z 0 1 
# z z 7 0 

# in
# 4 6
# 0 1 1
# 0 2 5
# 1 2 2
# 1 3 4
# 2 3 1
# 3 2 -7
# out
# Negarive Cycle

