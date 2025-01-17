from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m,n =3, 3
visited = [[False]*m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

bfs(0,0)
print(visited)
