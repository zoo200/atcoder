a = [3,5,1,4,2]

for i in reversed(range(len(a))):
    print(i)
    for j in range(i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

print(a)
