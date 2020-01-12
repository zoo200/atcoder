def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

a,b=map(int,(input().split()))
print(gcd(a,b))
