from collections import deque
from copy import deepcopy

grid = [[0] * 102 for _ in range(102)]
N = int(input())
# x, y, 방향, 세대
dragon = []
for _ in range(N):
    dragon.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for n in range(N):
    x, y, d, g = dragon[n]
    curve = [d]

    # 커브 방향 찾기
    for _ in range(g):
        for i in range(len(curve) - 1, -1, -1):
            curve.append((curve[i]+1) % 4)

    grid[y][x] = 1
    for c in curve:
        nx, ny = x + dx[c], y + dy[c]
        grid[ny][nx] = 1
        x, y = nx, ny


result = 0
for j in range(100):
    for i in range(100):
        if grid[j][i] and grid[j+1][i] and grid[j][i+1] and grid[j+1][i+1]:
            result += 1

print(result)