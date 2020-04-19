a, b, c, d = list(map(int, input().split()))

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)
 
def lcm(a, b):
    return a // gcd(a, b) * b

def calc(x,c,d):
    return x - x//c - x //d + x//lcm(c,d)

print(calc(b,c,d) - calc(a-1,c,d))
