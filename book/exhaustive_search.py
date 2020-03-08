# 5
# 1 5 7 10 21
# 4
# 2 4 17 8
# no
# no
# yes
# yes
n = int(input())
a = list(map(int,input().split()))[:n]
q = int(input())
m = list(map(int,input().split()))[:q]

def solve(i,m):
    if m == 0: return True
    elif i >= n: return False
    res = solve(i +1 ,m) or solve(i+1,m -a[i])
    return res

for x in m:
    if solve(0,x): print('yes')
    else: print('no')
