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
