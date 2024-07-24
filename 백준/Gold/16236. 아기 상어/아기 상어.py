from collections import deque

N = int(input())
sea = []
for _ in range(N):
    sea.append(list(map(int, input().split())))

shark_x, shark_y = -1, -1
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark_x = i
            shark_y = j
            sea[i][j] = 0

shark_size = 2

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global shark_size
    visited = [[False] * N for _ in range(N)]
    dist = [[-1] * N for _ in range(N)]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    dist[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if sea[nx][ny] > shark_size:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist


cnt = 0             # 몇 초 걸렸는 지
fish_cnt = 0        # 몇 마리 먹었는 지
while True:
    # [1] 현재 상어 위치 모든 좌표에 대한 거리 계산
    dist = bfs(shark_x, shark_y)

    # [2] 먹을 수 있는 물고기 확인
    eat = []
    for i in range(N):
        for j in range(N):
            if 1 <= sea[i][j] < shark_size and dist[i][j] != -1:
                eat.append((i, j))

    if len(eat) == 0:
        break
    elif len(eat) == 1:
        # [3-1] 먹을 수 있는 물고기 1개면 바로 이동
        fish_x, fish_y = eat[0]
        fish_cnt += 1
        fish_dist = dist[fish_x][fish_y]
        cnt += fish_dist

        shark_x = fish_x
        shark_y = fish_y
        sea[fish_x][fish_y] = 0
    else:
        # [3-2] 먹을 수 있는 물고기 2개 이상
        # 가장 작은 거리에 있는 물고기 선정
        min_dist = 10000

        for i, j in eat:
            if min_dist > dist[i][j]:
                min_dist = dist[i][j]
                min_x, min_y = i, j

        # 다음 위치 찾기
        for n in range(4):
            nx, ny = shark_x + dx[n], shark_y + dy[n]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if sea[nx][ny] > shark_size:
                continue
            if (nx, ny) == (min_x, min_y):
                shark_x, shark_y = nx, ny
                sea[nx][ny] = 0
                cnt += 1
                fish_cnt += 1
                break
            temp = bfs(nx, ny)
            if temp[min_x][min_y] == -1:
                break
            if (temp[min_x][min_y] + 1) == min_dist:
                shark_x, shark_y = nx, ny
                cnt += 1
                break



    # [3-3] 상어 크기 키우기
    if shark_size == fish_cnt:
        shark_size += 1
        fish_cnt = 0


# 최종
print(cnt)