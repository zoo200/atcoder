from collections import deque

h,w = map(int,input().split())
m = [input() for _ in range(h)]
q = deque()
# isset的なのないため予め定義しておいた方がやりやすい
vm = [[0] * w for _ in range(h) ]


for sy in range(h):
    for sx in range(w):
        if m[sy][sx] == 's':
            vm[sy][sx] = True
            q.append([sy,sx])

            while q:
                y,x = q.pop()
                for i,j in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                    xi , yj = x + i , y + j

                    if xi >= 0 and yj >= 0 and xi < w and yj < h and vm[yj][xi] == 0 and m[yj][xi] != "#":
                          if m[yj][xi] == 'g': 
                            print('Yes')
                            exit()
                          else:
                              vm[yj][xi] = True
                              q.append([yj,xi])

print('No')

# https://atc001.contest.atcoder.jp/tasks/dfs_a 
# 1 10
# s..####..g
# No

# 10 10
# s.........
# #########.
# #.......#.
# #..####.#.
# ##....#.#.
# #####.#.#.
# g.#.#.#.#.
# #.#.#.#.#.
# #.#.#.#.#.
# #.....#...
# Yes
