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
