from collections import deque
from copy import deepcopy

N, Q = map(int, input().split())
ice = []
for _ in range(2**N):
    ice.append(list(map(int, input().split())))
stage = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rotate(l, si, sj):
    global ice, n_ice

    for i in range(2**l):
        for j in range(2**l):
            # n_ice[si+i][si+j] = ice[sj+j][(2**l)-1-(si+i)]
            n_ice[si+j][sj+(2**l)-1-i] = ice[si+i][sj+j]


for s in stage:
    # [1] 격자 나누기 (시작 좌표 구하기)
    start_coord = []
    for i in range(0, 2**N, 2**s):
        for j in range(0, 2**N, 2**s):
            start_coord.append((i, j))

    # [2] 시작 좌표 기준, 시계 방향 90도 회전
    n_ice = [[0] * (2**N) for _ in range(2**N)]
    for si, sj in start_coord:
        rotate(s, si, sj)
    ice = n_ice

    n_ice = deepcopy(ice)
    # [3] 얼음이 있는 칸 3개 혹은 그 이상과 인접하지 않은 칸 => 얼음 - 1
    for i in range(2**N):
        for j in range(2**N):
            if ice[i][j] == 0:
                continue
            ice_o = 0
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if ni < 0 or ni >= 2**N or nj < 0 or nj >= 2**N:
                    continue
                if ice[ni][nj] > 0:
                    ice_o += 1
            if ice_o <= 2:
                n_ice[i][j] -= 1
    ice = n_ice

# [4-1] 남은 얼음 합
result = 0
for i in range(2**N):
    result += sum(ice[i])

# [4-2] 가장 큰 덩어리 차지 칸의 개수

visited = [[False] * 2**N for _ in range(2**N)]
n_result = 0

for i in range(2**N):
    for j in range(2**N):
        if ice[i][j] == 0:
            continue
        if visited[i][j]:
            continue
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        temp = 1

        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if nx < 0 or nx >= 2**N or ny < 0 or ny >= 2**N:
                    continue
                if visited[nx][ny]:
                    continue
                if ice[nx][ny] > 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    temp += 1
        if temp > n_result:
            n_result = temp

print(result)
print(n_result)