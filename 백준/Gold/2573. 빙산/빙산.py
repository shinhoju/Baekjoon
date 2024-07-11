from collections import deque

# 입력 받기
N, M = map(int, input().split())
ice = []
for _ in range(N):
    ice.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 다음 칸이 물일 때, -1
            if ice[nx][ny] == 0 and temp[x][y] != 0:
                temp[x][y] -= 1

            # 다음 칸이 얼음일 때, queue 삽입
            elif ice[nx][ny] >= 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return 1



flag = 0
year = 0

while True:
    visited = [[False] * M for _ in range(N)]
    result = []

    # 얼음 녹일 리스트
    temp = [x[:] for x in ice]

    for n in range(N):
        for m in range(M):
            if ice[n][m] != 0 and not visited[n][m]:
                result.append(bfs(n, m))

    ice = temp

    if len(result) == 0:
        break
    elif len(result) > 1:
        flag = 1
        break
    year += 1

if flag:
    print(year)
else:
    print(0)