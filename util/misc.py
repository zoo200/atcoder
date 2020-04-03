#---------------------
# 文字列反転
#---------------------
s='abcde'
print(s[::-1])

# edcba

#---------------------
# dict key sort
#---------------------
a={1: 5, 2: 4, 3: 1, 4: 0}
b=sorted(a.items())
# b=sorted(a.items(), reverse=True) # 逆順
# b=sorted(a.items(),key=lambda x:x[1])  # for Value
# b=sorted(a.items(),key=lambda x:x[1], reverse=True) # for Value Re

print(b)

for i,j in b:
    print(j)
    
# [(1, 5), (2, 4), (3, 1), (4, 0)]
# 5
# 4
# 1
# 0


