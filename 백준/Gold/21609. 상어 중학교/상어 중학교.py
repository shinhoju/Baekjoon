# 21609. 상어 중학교

from collections import deque

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def in_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True


def bfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = True
    cur_c = arr[x][y]
    g = [(x, y)]
    rb = []

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not in_range(nx, ny):
                continue
            if v[nx][ny]:
                continue
            # 무지개 or 일반 블록 (번호 =)
            if arr[nx][ny] == 0 or arr[nx][ny] == cur_c:
                q.append((nx, ny))
                v[nx][ny] = True
                g.append((nx, ny))
                if arr[nx][ny] == 0:
                    rb.append((nx, ny))

    # 무지개 칸 초기화
    for rx, ry in rb:
        v[rx][ry] = False

    if len(g) > 1:
        return g, len(rb)
    else:
        return [], len(rb)


def gravity(x, y, c):
    nx, ny = x + 1, y
    if not in_range(nx, ny):
        arr[x][y] = c
        return
    if arr[nx][ny] != -2:
        arr[x][y] = c
        return
    elif arr[nx][ny] == -2:
        gravity(nx, ny, c)



answer = 0
while True:
    # 블록 그룹이 존재할 때 까지 오토 플레이
    # [1] 블록 그룹 찾기
    groups = {}
    v = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j] and arr[i][j] > 0:
                group, r = bfs(i, j)
                if group:
                    groups[(i, j, r)] = group
    if not groups:
        break

    # [2] 가장 큰 블록 그룹 찾기
    # 무지개 블록 갯수 / 기준 블록 행 큰 거 / 열 큰 거
    mx_group = []
    mx_i = mx_j = -1
    rainbows = 0
    for (i, j, r), group in groups.items():
        if len(group) > len(mx_group):
            mx_group = group
            mx_i, mx_j = i, j
            rainbows = r
        elif len(group) == len(mx_group):
            if r > rainbows:
                rainbows = r
                mx_group = group
                mx_i, mx_j = i, j
            elif r == rainbows:
                if i > mx_i:
                    mx_i, mx_j = i, j
                    mx_group = group
                    rainbows = r
                elif i == mx_i:
                    if j > mx_j:
                        mx_i, mx_j = i, j
                        mx_group = group
                        rainbows = r

    # [3] 그룹의 모든 블록 제거
    answer += (len(mx_group) ** 2)
    for i, j in mx_group:
        arr[i][j] = -2

    # [4] 중력 작용
    for i in range(N-2, -1, -1):
        for j in range(N):
            if arr[i][j] >= 0:
                cur_c = arr[i][j]
                arr[i][j] = -2
                gravity(i, j, cur_c)

    # [5] 90도 반시계 회전
    n_arr = [[-3] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            n_arr[N-1-j][i] = arr[i][j]

    # [6] 중력 작용
    arr = n_arr
    for i in range(N-2, -1, -1):
        for j in range(N):
            if arr[i][j] >= 0:
                cur_c = arr[i][j]
                arr[i][j] = -2
                gravity(i, j, cur_c)

print(answer)