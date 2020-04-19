a = int(input())
b = list(map(int,input().split()))
sum=cnt=0

for i in b[:a]:
    sum = (sum|i)

while (sum&1) == 0:
    sum=(sum>>1)
    cnt += 1

print(cnt)

# Non bit 演算
# a = int(input())
# b = list(map(int,input().split()))
# cnt = 0
# is_even = True

# while is_even:
#     tmp = []
#     for i in b[:a]:

#         if i % 2:
#             is_even=False
#             break
#         else:
#             tmp.append(i//2)

#     if is_even:
#         cnt+=1
#         b = tmp

# print(cnt)
