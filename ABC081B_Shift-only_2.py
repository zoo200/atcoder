a = int(input())
b = list(map(int,input().split()))
sum=cnt=0

for i in b[:a]:
    sum = (sum|i)

while (sum&1) == 0:
    sum=(sum>>1)
    cnt += 1

print(cnt)