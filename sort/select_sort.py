a = [3,5,1,4,2,9]


for i in range(len(a)-1):
    print(i)
    for j in range(i+1,len(a)):
        print(j)
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]

print(a)
