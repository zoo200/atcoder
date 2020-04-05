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
