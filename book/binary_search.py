n=int(input())
s=list(map(int,input().split()))[:n]
q=int(input())
t=list(map(int,input().split()))[:n]

cnt=0

for key in t:

    left = 0
    right =n

    while left < right:
        mid = (left + right) //2
        if key == s[mid]:cnt+=1 ; break
        elif key > s[mid]: left = mid+1
        elif key < s[mid]: right = mid

print(cnt)

# p.122

# in
# 5
# 1 2 3 4 5
# 3
# 3 4 1

# out
# 3
