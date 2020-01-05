n,y=map(int,input().split())
is_none=True

for i in range(n+1):
    ai=10000*i
    if ai > y: continue
    else:
        for j in range(n+1-i):
            bj=5000*j
            if ai + bj > y :break
            else : 
                k=n-i-j
                if  ai + bj + 1000*k == y:
                    is_none=False
                    break
        if not is_none:break

if is_none:print(-1,-1,-1)
else: print(i,j,k)


