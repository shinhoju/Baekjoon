# 21609. 상어 중학교

from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
blocks = []
for _ in range(N):
    blocks.append(list(map(int, input().split())))
# -1: 검은색 블록, 0: 무지개 블록, M: 색깔 갯수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True


def bfs(x, y):
    global visited, blocks

    group = [(x, y)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    color = blocks[x][y]
    rainbow = []

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not in_range(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if blocks[nx][ny] == color or blocks[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                group.append((nx, ny))
                if blocks[nx][ny] == 0:
                    rainbow.append((nx, ny))

    # debug: 무지개 블록의 visited 초기화
    for x, y in rainbow:
        visited[x][y] = False

    return group, len(rainbow)


def dfs(x, y):
    global blocks
    nx, ny = x + 1, y
    if in_range(nx, ny):
        if blocks[nx][ny] == -2:
            return dfs(nx, ny)
        else:
            return x, y
    elif nx == N:
        return x, y


score = 0
while True:
    # [1] 블록 그룹 찾기
    visited = [[False] * N for _ in range(N)]
    block_group = []
    block_rainbow = 0
    for i in range(N):
        for j in range(N):
            # 아무 것도 없는 칸이면 패스
            if blocks[i][j] <= 0:
                continue

            temp_group, num_r = bfs(i, j)
            if len(temp_group) > len(block_group):
                block_group = temp_group
                block_rainbow = num_r
            elif len(temp_group) == len(block_group):
                # 무지개 블록의 수가 가장 많은 블록 그룹
                if num_r > block_rainbow:
                    block_rainbow = num_r
                    block_group = temp_group
                elif num_r == block_rainbow:
                    # 기준 블록의 행이 가장 큰 것
                    if temp_group[0][0] > block_group[0][0]:
                        block_group = temp_group
                        block_rainbow = num_r
                    elif temp_group[0][0] == block_group[0][0]:
                        # 기준 블록의 열이 가장 큰 것
                        if temp_group[0][1] > block_group[0][1]:
                            block_group = temp_group
                            block_rainbow = num_r
    # [1-1] 블록 그룹이 없을 때 멈춤
    if len(block_group) <= 1:
        break

    # [2] 1에서 찾은 블록 삭제, 점수 획득
    for i, j in block_group:
        blocks[i][j] = -2
    score += (len(block_group))**2

    # [3] 중력 작용
    for i in range(N-2, -1, -1):
        for j in range(N):
            if blocks[i][j] >= 0:
                ni, nj = dfs(i, j)
                if (ni, nj) != (i, j):
                    blocks[ni][nj] = blocks[i][j]
                    blocks[i][j] = -2

    # [4] 90도 반시계 방향 회전
    n_blocks = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            n_blocks[i][j] = blocks[j][N-1-i]

    blocks = n_blocks

    # [5] 다시 중력 작용
    for i in range(N-2, -1, -1):
        for j in range(N):
            if blocks[i][j] >= 0:
                ni, nj = dfs(i, j)
                if (ni, nj) != (i, j):
                    blocks[ni][nj] = blocks[i][j]
                    blocks[i][j] = -2

print(score)