n,a,b = map(int,input().split())
res=0

for i in range(1,n+1):
    c = sum(list(map(int,list(str(i)))))
    if a <= c <= b:res+=i

print(res)
