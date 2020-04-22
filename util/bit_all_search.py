# https://drken1215.hatenablog.com/entry/2019/12/14/171657
# n 個の数値　合計してw になるか
n,w=map(int,input().split())
a = list(map(int,input().split()))[:n]

f=False

# 1<<3 => 8 つまり7(111) までを全部調べる
for i in range((1 << n)):
    sum =0

    
    for j in range(n):
        # e.g. i=3 (011) を (001),(010),(100)  でぶつけてふるい落とす
        # j桁目のbitが経っていたらその番目の数値足す     
        if i & (1 << j): sum +=a[j]

    if sum == w: f=True

if f :print('Yes')
else: print('No')
