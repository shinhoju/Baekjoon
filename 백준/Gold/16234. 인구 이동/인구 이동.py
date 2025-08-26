# 16234. 인구이동

from collections import deque

N, L, R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# unit = bfs(i, j)
def bfs(x, y):
    global v, arr
    u = [(x, y)]
    u_sum = arr[x][y]
    q = deque()
    q.append((x, y))
    v[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 조건: L <= 인구 차이 <= R
            if not v[nx][ny] and L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                u.append((nx, ny))
                u_sum += arr[nx][ny]
                q.append((nx, ny))
                v[nx][ny] = True
    return u, u_sum


result = 0
while True:
    # [1] 연합 구하기
    v = [[False] * N for _ in range(N)]
    units = []
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                unit, unit_sum = bfs(i, j)
                if len(unit) > 1:
                    units.append((unit, unit_sum))

    # [2] 연합 없으면 인구 이동 X => 종료 조건
    if not len(units):
        break

    # [3] 인구 이동
    for unit, unit_sum in units:
        tmp_pop = unit_sum // len(unit)
        for ux, uy in unit:
            arr[ux][uy] = tmp_pop

    result += 1

print(result)
