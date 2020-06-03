#---------------------
# 判定
#---------------------
import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


print(is_prime(3))

#---------------------
# 因数分解
#---------------------
# 再帰方式
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

# 10**16+7 で試したら再帰のほうが断然早い メモリ使用量も10.5 MiB くらいで変わらず  
% time python test.py
[53, 113, 277, 1117, 5396507]
python test.py  0.04s user 0.04s system 95% cpu 0.080 total
% time python test.py
[53, 113, 277, 1117, 5396507]
python test.py  5.85s user 0.05s system 99% cpu 5.919 total
% 


#---------------------
# エラストテネスの篩
#---------------------
def sieve(n):
    num = [True]*n
    num[0] = num[1] = False
    for i in range(2,int(n**0.5)+1):
        if num[i]:
            for j in range(i**2, n, i):
                num[j] = False
    return [i for i in range(2,n) if num[i]]

