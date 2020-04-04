n,q=map(int,input().split())

# root番号保持
p = list(range(n))
# 階層保持
rank =  [0] * n
# ノード数
node =  [1] *n

def find_set(x):
    if(x != p[x]):
        p[x] = find_set(p[x])
    return p[x]

def unite(x,y):
    link(find_set(x),find_set(y))

def link(x,y):
    if rank[x] > rank[y]:
        p[y] =x
        node[x] += node[y] 
    else:
        p[x] = y
        node[y] += node[x] 
        if rank[x] == rank[y]:
            rank[y] +=1

def same(x,y):
    return find_set(x) == find_set(y)

print(p)
print(rank)
print(node)

for i in range(q):
    t,a,b = map(int,input().split())

    if t == 0: unite(a,b)
    elif(t==1):
        if same(a,b):print(1)
        else: print(0)
    print()
    print(p)
    print(rank)
    print(node)

#ABC157_D_Friend_Suggestions の改良版のほうがいいかも
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
# 0
# 0
# 1
# 1
# 1
# 0
# 1
# 1
