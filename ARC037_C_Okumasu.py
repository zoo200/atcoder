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
