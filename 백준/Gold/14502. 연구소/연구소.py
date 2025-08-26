# 14502. 연구소

from collections import deque

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 바이러스 / 빈 칸 위치 찾기
virus = []
empty = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
        if arr[i][j] == 0:
            empty.append((i, j))


def comb(a, n):
    result = []
    if len(a) < n:
        return result

    if n == 1:
        for i in a:
            result.append([i])

    elif n > 1:
        for i in range(len(a) - n + 1):
            for j in comb(a[i + 1:], n - 1):
                result.append([a[i]] + j)

    return result


def bfs(x, y):
    global v, n_arr
    q = deque()
    q.append((x, y))
    v[x][y] = True

    while q:
        x, y = q.popleft()
        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 방문 x / 빈 칸이면 바이러스 퍼짐
            if not v[nx][ny] and n_arr[nx][ny] == 0:
                v[nx][ny] = True
                n_arr[nx][ny] = 2
                q.append((nx, ny))


# 벽을 세울 세 칸 고르기
safe_area = 0
for w1, w2, w3 in comb(empty, 3):
    n_arr = [a[:] for a in arr]
    for i, j in (w1, w2, w3):
        n_arr[i][j] = 1

    # 바이러스 퍼트리기
    v = [[False] * M for _ in range(N)]
    for vx, vy in virus:
        bfs(vx, vy)

    # 안전 지대 계산
    tmp_safe = 0
    for i in range(N):
        for j in range(M):
            if n_arr[i][j] == 0:
                tmp_safe += 1

    if tmp_safe > safe_area:
        safe_area = tmp_safe

print(safe_area)
