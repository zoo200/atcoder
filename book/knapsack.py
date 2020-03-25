from collections import defaultdict

n,w = map(int,input().split())
items = defaultdict(dict)
c = [[0] * (w +1) for _ in range(n+1) ]
g = [[0] * (w +1) for _ in range(n+1) ]

for i in range(1,n+1):
    a,b = map(int,input().split())
    items[i]['v'] = a
    items[i]['w'] = b

for i in range(w+1):
    c[0][i] = 0
    g[0][i] = 1

for i in range(1,n+1):
    c[i][0] = 0

for i in range(1,n+1):
    for j in range(1,w+1):
        c[i][j] = c[i-1][j]
        g[i][w] = 0

        if(items[i]['w'] > j): continue

        # 一つ前のアイテムまでが入ってるナップザックに今のアイテム重量が入ったときのナップザックの価値
        now_v = items[i]['v'] + c[i-1][j- items[i]['w']]

        # 入れないより入れたほうが価値が高い
        if( now_v > c[i-1][j]):
            c[i][j] = now_v
            g[i][j] = 1

# 最大価値
max_v = c[n][w]
print(max_v)

[print(i) for i in c]
[print(i) for i in g]

# どれを選べば最大価値か逆順でたどっていく
p = []
ww = w
for i in range(n,0,-1):
    if(g[i][ww] == 1):
        p.append(i)
        ww -= items[i]['w']

print(p)

# p.416

# in
# 4 5
# 4 2
# 5 2
# 2 1
# 8 3

# out
# 13
# [0, 0, 0, 0, 0, 0]
# [0, 0, 4, 4, 4, 4]
# [0, 0, 5, 5, 9, 9]
# [0, 2, 5, 7, 9, 11]
# [0, 2, 5, 8, 10, 13]
# [1, 1, 1, 1, 1, 1]
# [0, 0, 1, 1, 1, 1]
# [0, 0, 1, 1, 1, 1]
# [0, 1, 0, 1, 0, 1]
# [0, 0, 0, 1, 1, 1]
# [4, 2]
