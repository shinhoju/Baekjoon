# 16234. 인구이동

from collections import deque
from copy import deepcopy

N, L, R = map(int, input().split())
country = []
for _ in range(N):
    country.append(list(map(int, input().split())))

# 인구 이동이 며칠 동안 발생하는지 카운팅
cnt = 0

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global dx, dy, visited

    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    temp_pairs = [(x, y)]
    temp_sum = country[x][y]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if L <= abs(country[x][y] - country[nx][ny]) <= R:
                temp_pairs.append((nx, ny))
                queue.append((nx, ny))
                visited[nx][ny] = True
                temp_sum += country[nx][ny]

    return temp_pairs, temp_sum


while True:
    # [1] 연합 구하기
    pairs = set()
    pair_sum = dict()

    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                temp, summ = bfs(i, j)
                if len(temp) > 1:
                    pair_sum[tuple(sorted(temp))] = summ
                    pairs.add(tuple(sorted(temp)))

    if len(pairs) < 1:
        break
    else:
        cnt += 1

    # [2] 인구 이동: 인구수 = (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
    new_country = deepcopy(country)
    for p in pairs:
        new_population = pair_sum[p] // len(p)
        for px, py in p:
            new_country[px][py] = new_population
    country = new_country

print(cnt)