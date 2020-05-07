import sys
sys.setrecursionlimit(100000)

n=int(input())

g =[[] for _ in range(n)]
ans=[0] * (n-1)

def dfs(v,c=-1,p=-1):
    k=1

    for u,ei in g[v]:
        if u == p: continue # nodeがcall元の親と一致してたらスルー
        if k == c: k+=1 # 色を塗る

        ans[ei] = k
        k+=1   # 次の色
        dfs(u,ans[ei],v)

for i in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    g[a].append((b,i))
    g[b].append((a,i))
print(g)
dfs(0)
mx=0

for i in range(n):
    mx = max(mx,int(len(g[i])))

print(mx)
for i in ans:print(i)
