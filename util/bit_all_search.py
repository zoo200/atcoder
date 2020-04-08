# https://drken1215.hatenablog.com/entry/2019/12/14/171657
n,w=map(int,input().split())
a = list(map(int,input().split()))[:n]

f=False

for i in range((1 << n)):
    sum =0

    for j in range(n):
        if i & (1 << j): sum +=a[j]

    if sum == w: f=True

if f :print('Yes')
else: print('No')
