from collections import deque

N, L, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    temp = set()
    temp.add((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not in_range(nx, ny):
                continue
            if not visited[nx][ny]:
               if L <= abs(A[x][y] - A[nx][ny]) <= R:
                    temp.add((nx, ny))
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    units.append(temp)


cnt = 0
while True:
    # [1] 좌 하 상 우 에 있는 국가 중 인구 차이가 L 이상 R 이하일 때 연합
    units = []          # 연합 리스트 담을 리스트
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    ones = 0
    for unit in units:
        if len(unit) == 1:
            ones += 1
            continue

        sum_v = 0
        for ux, ny in unit:
            sum_v += A[ux][ny]

        ppl = sum_v // len(unit)
        for ux, ny in unit:
            A[ux][ny] = ppl

    # 종료 조건 : 더 이상 인구 이동 불가능 할 때
    if ones == (N * N):
        break

    cnt += 1


print(cnt)