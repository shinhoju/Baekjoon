N, M = map(int, input().split())
office = []
# 1~5: cctv, 6: 벽, -1: 감시 가능
for _ in range(N):
    office.append(list(map(int, input().split())))

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv 유형 분류
move = [[],
        [0, 1, 2, 3],
        [(0, 2), (1, 3)],
        [(0, 1), (1, 2), (2, 3), (3, 0)],
        [(3, 0, 1), (0, 1, 2), (1, 2, 3), (2, 3, 0)],
        [(0, 1, 2, 3)]]

cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv.append((i, j))


def count_zero(arr):
    cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                cnt += 1
    return cnt


def in_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    else:
        return True


def fill(x, y, m, arr):
    if type(m) is int:
        while True:
            nx, ny = x + dx[m], y + dy[m]
            if not in_range(nx, ny):
                break
            if office[nx][ny] == 6:
                break
            arr[nx][ny] = -1
            x, y = nx, ny
    else:
        for mm in m:
            mx, my = x, y
            while True:
                nx, ny = mx + dx[mm], my + dy[mm]
                if not in_range(nx, ny):
                    break
                if office[nx][ny] == 6:
                    break
                if arr[nx][ny] == 0:
                    arr[nx][ny] = -1
                mx, my = nx, ny

    return arr


def dfs(depth, arr):
    global min_value, cctv, move, dx, dy
    if depth == len(cctv):
        value = count_zero(arr)
        min_value = min(value, min_value)
        return

    cx, cy = cctv[depth]
    c_num = office[cx][cy]
    for m in move[c_num]:
        temp = [a[:] for a in arr]
        temp = fill(cx, cy, m, temp)
        dfs(depth + 1, temp)


min_value = 100000
dfs(0, office)
print(min_value)