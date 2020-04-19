from collections import deque

r,c = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
m = [input() for _ in range(r)]
sy += -1
sx += -1
gy += -1
gx += -1

q = deque()
vm = [[-1] * c for _ in range(r)]

vm[sy][sx] = 0
q.append([sy,sx])

while q:
    y,x = q.popleft()

    if x == gx and y == gy:
          print(vm[y][x])
          exit()

    for i,j in ([1, 0], [-1, 0], [0, 1], [0, -1]):
        xi , yj = x + i , y + j
        if xi >= 0 and yj >= 0 and xi < c and yj < r and vm[yj][xi] == -1 and m[yj][xi] != "#":
            vm[yj][xi] = vm[y][x] + 1
            q.append([yj,xi])

