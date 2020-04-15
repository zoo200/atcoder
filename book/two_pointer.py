n,s=map(int,input().split())
a=[int(input()) for _ in range(n)]

if 0 in a:print(n);exit()
if a[0] > s: print(0);exit()

sum=1
right=0
res=0

# アタマの移動
for k,v in enumerate(a):

    # ケツの移動
    while right < n and sum * a[right] <= s:
        sum *= a[right]
        right+=1

    # ケツ - アタマ　で距離求める
    res = max(res, right - k)

    # アタマがケツに追いついた
    if right == k:
        right=+1
        
    # アタマすすめるのでその分、減らす（この問題では割る)
    else:
        sum //= v
    
print(res)

# https://atcoder.jp/contests/abc032/submissions/11869390
