import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline      


a = int(input())

a,b = map(int,input().split())

a = list(map(int,input().split()))

n = int(input())
a = list(map(int,input().split()))[:n]

a = int(input())
b = [int(input()) for _ in range(a)]
# 2
# 1
# 2
# [1, 2]

n = int(input())
m = [[0] * n for _ in range(n) ]
# 3
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


dp = [[[0] * 4 for _ in range(3)] for _ in range(2)]
print(dp)
# 3次元
#[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

m = [list(map(int,input().split())) for _ in range(3)]
print(m)
# in
# 84 97 66
# 79 89 11
# 61 59 7
# out
# [[84, 97, 66], [79, 89, 11], [61, 59, 7]]

n = int(input())
d = [list(map(int,input().split())) for i in range(n)]
d.sort(key=lambda x: x[1])
print(d)
# in
# 5
# 2 4
# 1 9
# 1 8
# 4 9
# 3 12
# out dict じゃなくもsort使える
# [[2, 4], [1, 8], [1, 9], [4, 9], [3, 12]]

j = [1,2,3,4]
for i in j:
    print(i,end=" ")
print()
print([i*2 for i in j])
print(" ".join([str(i*2) for i in j]))
print(" ".join(map(str,j)))
# 1 2 3 4 
# [2, 4, 6, 8]
# 2 4 6 8
# 1 2 3 4
