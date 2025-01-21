# 톱니바퀴 (시뮬레이션, 구현, dfs)
# 구하는 것: K번 회전 시킨 후, 점수 구하기


from copy import deepcopy
from collections import deque

gears = []
for _ in range(4):
    gears.append(list(map(int, input())))

K = int(input())
move = []
for _ in range(K):
    a, b = map(int, input().split())
    move.append([a-1, b])


def bfs(idx, dirs):
    visited = [False] * 4
    rotate = [0] * 4            # 0: 안돌림, 1: 시계, -1: 반시계
    queue = deque()
    queue.append((idx, dirs))
    visited[idx] = True
    rotate[idx] = dirs

    while queue:
        idx, dirs = queue.popleft()
        for n in [-1, 1]:
            n_idx = idx + n
            if n_idx < 0 or n_idx >= 4:
                continue
            if visited[n_idx]:
                continue

            if n == -1 and gears[idx][6] != gears[n_idx][2]:
                visited[n_idx] = True
                n_dirs = 1 if dirs == -1 else -1
                queue.append((n_idx, n_dirs))
                rotate[n_idx] = n_dirs

            if n == 1 and gears[idx][2] != gears[n_idx][6]:
                visited[n_idx] = True
                n_dirs = 1 if dirs == -1 else -1
                queue.append((n_idx, n_dirs))
                rotate[n_idx] = n_dirs

    return rotate


def rotation(r):
    for i, g in enumerate(r):
        if g == 0:
            continue

        temp = [0] * 8

        if g == 1:
            for j in range(8):
                temp[(j+1) % 8] = gears[i][j]
        else:
            for j in range(8):
                temp[(j+7) % 8] = gears[i][j]


        gears[i] = temp


# [1] 톱니바퀴 회전
for g_idx, g_dir in move:
    # [1-1] 어느 바퀴 회전 해야 하는지 확인
    rotate_gears = bfs(g_idx, g_dir)
    rotation(rotate_gears)

# 점수 구하기
result = 0
for i in range(4):
    if gears[i][0] == 1:
        result += 2**i

print(result)