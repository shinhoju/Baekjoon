from collections import deque
from itertools import combinations

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_virus():
    global n_maps
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if n_maps[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = True
                cnt += 1

    while queue:
        x, y = queue.popleft()
        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and n_maps[nx][ny] == 0:
                n_maps[nx][ny] = 2
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    return cnt

# 3개의 연구소 세우기
walls = 0
empty = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            empty.append((i, j))
        if maps[i][j] == 1:
            walls += 1

for es in combinations(empty, 3):
    n_maps = [m[:] for m in maps]
    for ex, ey in es:
        n_maps[ex][ey] = 1
    vir = count_virus()
    cnt = max((N*M-vir-walls-3), cnt)

print(cnt)