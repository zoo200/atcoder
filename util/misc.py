#---------------------
# 文字列反転
#---------------------
s='abcde'
print(s[::-1])

# edcba

#---------------------
# 辞書 sort
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

#---------------------
# list sort
#--------------------
c=sorted(b,key=lambda x: x[0],reverse=True)
# もしくは
b.sort(key=lambda x: x[0],reverse=True)

#---------------------
# 文字列str を数値へ変換
#---------------------
print(r)
for i,j in k.items():
    r[i-1] = j
print(k)
print(r)
print(int(''.join(r)))
# ['1', '0', '0']
# {1: '7', 3: '2'}
# ['7', '0', '2']
# 702
