from bisect import bisect_right
N, K = map(int, input().split())
a = sorted(map(int, input().split()))
b = list(map(int, input().split()))
 
ok, ng = 10**18 + 1, 0

while ok - ng > 1:
    x = (ok + ng) // 2
    total = 0
    for n in b:
        total += bisect_right(a, x // n)
 
    if total >= K:
        ok = x
    else:
        ng = x
 
print(ok)

# 以下だとTLE
# c = []
# for i in a:
#     for j in b:
#         c.append(i*j)
# c.sort()

# while ok - ng > 1:
#     x = (ok + ng) // 2
#     total = bisect_right(c, x)
 
#     if total >= K:
#         ok = x
#     else:
#         ng = x
 
# print(ok)


### 以下のようにするとbisect_right 同等
# def calc(x):
#     l,r = -1,N*N
#
#     while r-l > 1:
#         c = (r + l) // 2
#         if cl[c] <= x: 
#             l = c
#         else:       
#             r = c
#     return l+1
#
# while ok - ng > 1:
#     x = (ok + ng) // 2
#     # total = bisect_right(cl, x)
#     total = calc(x)
# 
#     if total >= K:
#         ok = x
#     else:
#         ng = x
 
