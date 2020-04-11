def pow(x, n):
    ans = 1
    while n:
        # print('aaa',x,n)
        if n % 2:
            ans *= x
            # print('bbb',ans)
        x *= x
        # print('ccc',x)
        n >>= 1
    return ans

print(pow(2,31))
