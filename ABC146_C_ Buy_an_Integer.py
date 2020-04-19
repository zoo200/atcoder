a,b,x=map(int,input().split())

l = 0
r = 10**9 + 1
while r - l > 1:
    c = (l + r) //2

    if a * c + b * len(str(c)) <= x:
        l = c
    else:
        r = c

print(l)

