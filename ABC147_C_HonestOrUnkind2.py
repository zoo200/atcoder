from collections import defaultdict

n=int(input())
d=defaultdict(list)

for i in range(n):
    a=int(input())

    for _ in range(a):
        x,y = map(int,input().split())
        d[i].append((x-1,y))

res=0

# e.g. ３人であれば(000)全員嘘不親切と仮定) ~ (111)全員正直と仮定)　まですべて調べる。
for i in range(1<<n):
    bf=False

    for j in range(n):

        # 正直者(と仮定した) の発言者の矛盾を調べる
        # e.g. 011  に010 をぶつける
        if (i>>j)&1 == 1:
            
            # e.g. ２人目の発言内容(011 & 010)
            for x,y in d[j]:
                # 正直者の発言内容と違う　e.g. x=2,y=1 で i=011 の場合2人目が0 なので矛盾している
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
