a = int(input())
b = list(map(int,input().split()))
cnt = 0
is_even = True

while is_even:
    tmp = []
    for i in b[:a]:

        if i % 2:
            is_even=False
            break
        else:
            tmp.append(i//2)

    if is_even:
        cnt+=1
        b = tmp

print(cnt)
