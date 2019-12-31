a = [3,5,1,4,2,9,6,8]

h = len(a) // 2

while h > 0:
    for i in range(h,len(a)):
        while i >= h and a[i] < a[i - h]:
            a[i - h] , a[i] = a[i],a[i - h]
            i -= h
    h //=2

print(a)
