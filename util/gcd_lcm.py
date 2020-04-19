def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

a,b=map(int,(input().split()))
print(gcd(a,b))


# こっちのほうがかっこいい
def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

# a*b // gcd(a,b) だと a*b したときにオーバーフローする可能性があるため
def lcm(a, b):
    return a // gcd(a, b) * b
