import itertools

print(list(itertools.permutations(['a','b','c'])))
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

print(list(itertools.permutations(range(3))))
# [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

for i in itertools.permutations(range(3)):
    print(i)
# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)

### なんか連結したいとき ##
n=3
nn=[]
ss=[]
for i in range(1,n+1):
      nn.append(i)
print(nn)
for i in itertools.permutations(nn):
    print(i)
    ss.append(''.join(map(str,list(i))))
 
print(ss)
# [1, 2, 3]
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)
# ['123', '132', '213', '231', '312', '321']
######################

print(list(itertools.permutations(range(3),2)))
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

print(list(itertools.permutations(['a','a','c'])))
# [('a', 'a', 'c'), ('a', 'c', 'a'), ('a', 'a', 'c'), ('a', 'c', 'a'), ('c', 'a', 'a'), ('c', 'a', 'a')]

print(list(itertools.combinations(['a','a','c'],3)))
# [('a', 'a', 'c')]

print(list(itertools.permutations(['a','a','c'],2)))
# [('a', 'a'), ('a', 'c'), ('a', 'a'), ('a', 'c'), ('c', 'a'), ('c', 'a')]

print(list(itertools.combinations(['a','a','c'],2)))
# 位置で判別してる模様
# [('a', 'a'), ('a', 'c'), ('a', 'c')]


import math

def perm(x,y):
    return math.factorial(x) // math.factorial(x - y)

def comb(x,y):
    return math.factorial(x) // (math.factorial(x - y) * math.factorial(y))

# 最初から２通りしか選ばない場合は以下
def comb(x):
    return x * (x - 1) // 2


print(math.factorial(5))
print(perm(5,2))
print(comb(5,2))
# 120
# 20
# 10
