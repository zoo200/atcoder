a=input()
n=len(a)

for i in range(1<<n):
    sum=0
    st=''
    for j in range(n):

        # if i & (1 <<j):sum +=int(a[j]); st+= '+' + a[j] 
        # else: sum -=int(a[j]); st+= '-' + a[j]
        if i & (1 <<j):st+= '+' + a[j] 
        else:  st+= '-' + a[j]

    # if sum==7:break
    if eval(st[1:]) == 7:break

print(st[1:] + '=7')
