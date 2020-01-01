n,a,b = map(int,input().split())
res=0

for i in range(1,n+1):
    sum=0
    for j in list(str(i)):sum+=int(j)
    if a <= sum <= b:res+=i

print(res)
