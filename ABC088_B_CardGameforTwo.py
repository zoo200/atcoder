n=int(input())
a = list(map(int,input().split()))[:n]
a.sort(reverse=True)

A=B=I=0
for i in a:
    if I %2:B+=i
    else:A+=i
    I+=1

print(A-B)
# other
# print(sum(a[::2]) - sum(a[1::2]))
