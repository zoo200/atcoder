from collections import defaultdict

n=int(input())
d=defaultdict(list)

for i in range(n):
    a=int(input())

    for _ in range(a):
        x,y = map(int,input().split())
        d[i].append((x-1,y))

res=0
for i in range(1<<n):
    bf=False

    for j in range(n):

        # 正直者の発言の矛盾を調べる
        if (i>>j)&1 == 1:
            for x,y in d[j]:
                # 正直者の発言内容と違う
                if (i>>x)&1 != y: 
                    bf=True
                    break
            if bf:break 

    if not bf:
        res=max(res,bin(i).count("1"))
        # シフト演算利用
        # count=0
        # for m in range(n):
        #     if (i & (1 << m)) : count+=1
        #     res=max(res,count)


print(res)
