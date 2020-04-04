n,q=map(int,input().split())

# root番号保持
p = list(range(n))
# 階層保持
rank =  list(range(n))

def find_set(x):
    if(x != p[x]):
        p[x] = find_set(p[x])
    return p[x]

def unite(x,y):
    link(find_set(x),find_set(y))

def link(x,y):
    if rank[x] > rank[y]:
        p[y] =x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] +=1

def same(x,y):
    return find_set(x) == find_set(y)

for i in range(n):
    p[i] = i # この実装だと実際は不要。本に書いてあったから残
    rank[i] =0

print(p)
print(rank)

for i in range(q):
    t,a,b = map(int,input().split())

    if t == 0: unite(a,b)
    elif(t==1):
        if same(a,b):print(1)
        else: print(0)

print(p)
print(rank)

# p.318
# in
# 5 12
# 0 1 4
# 0 2 3
# 1 1 2
# 1 3 4
# 1 1 4
# 1 3 2
# 0 1 3
# 1 2 4
# 1 3 0
# 0 0 4
# 1 0 2
# 1 3 0

# out
# [0, 1, 2, 3, 4]
# [0, 0, 0, 0, 0]
# 0
# 0
# 1
# 1
# 1
# 0
# 1
# 1
# [3, 4, 3, 3, 3]
# [0, 0, 0, 2, 1]
