# import decimal
# すべてOK
# a,b = map(decimal.Decimal,input().split())
# print(int(n*k))

# in1 はOK in2は9.79*100が978.99999 になってNG (逆に素直にa*b/100でいけるin2は。。。)
# a,b = map(float,input().split())
# print(int(a)*int(b*100)//100)

# これが想定解
a,b = input().split()
a=int(a)
b=int(b.replace(".",""))
print(a*b//100)

# in 1
# 999990000000001 9.99
# out
# 9989900100000009

# in 2
# 664706138336385 9.79
# out
# 6507473094313209
