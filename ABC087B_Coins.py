a,b,c,x = map(int,input().split())
cnt=0
for aa in range(a+1):
    for bb in range(b+1):
        for cc in range(c+1):
            if aa*500+bb*100+cc*50 == x:cnt+=1

print(cnt)
