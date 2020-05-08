import math

r=[]

def get_prime(n):
    if n == 1: return
    ff=False
    for k in range(2, int(math.sqrt(n)) + 1):

        if n % k == 0:
            r.append(k)
            get_prime(n/k)
            ff=True
            break

    # 割り切れなかったらそれが素数
    if not ff:
        r.append(int(n))

    return

get_prime(int(input()))
print(r)

# ループ方式
def factorization(n):
    if n < 2:
        return []

    res = []

    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            res.append(i)
            n //= i

    if n > 1:
        res.append(n)

    return res


