"""
익은 토마토 상 하 좌 우 위 아래의 안익은 토마토 --> 하루가 지나면 익음
한 턴 (하루)에 대해 모든 격자의 토마토 상태 update 필요
모든 토마토 익은 날 파악, return

초기 상태 --> 토마토 상태 파악, update --> 다음 날

3차원 리스트 필요

0: 안 익은 토마토
1: 익은 토마토
-1: 토마토 없는 칸
"""
from collections import deque

M, N, H = map(int, input().split())
graph = []
temp = []

for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, input().split())))
    graph.append(temp)

# 좌 우 상 하 위 아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

visited = [[[False] * M for _ in range(N)] for _ in range(H)]
queue = deque()

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H:
                continue

            if (not visited[nz][ny][nx]) and graph[nz][ny][nx] == 0:
                queue.append((nx, ny, nz))
                graph[nz][ny][nx] = graph[z][y][x] + 1
                visited[nz][ny][nx] = True

# 토마토 있는 위치 queue 담음
for k in range(H):
    for j in range(N):
        for i in range(M):
            if graph[k][j][i] == 1 and (not visited[k][j][i]):
                queue.append((i, j, k))
                visited[k][j][i] = True

bfs()

# 토마토 확인
result = 0
for k in graph:
    for j in k:
        for i in j:
            if i == 0:
                print(-1)
                exit()
        result = max(result, max(j))

print(result - 1)