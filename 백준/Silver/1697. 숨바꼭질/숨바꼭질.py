from collections import deque

MAX_POINTS = 100000
N, K = map(int, input().split())

maps = [0] * (MAX_POINTS + 1)

def bfs(x):
    ev = [lambda x: x - 1, lambda x: x + 1, lambda x: 2 * x]
    visited = [False] * (MAX_POINTS + 1)

    queue = deque()
    queue.append(N)
    visited[N] = True

    while queue:
        x = queue.popleft()
        for i in range(3):
            nx = ev[i](x)
            if nx < 0 or nx > MAX_POINTS:
                continue

            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
                maps[nx] = maps[x] + 1
    return maps[K]



result = bfs(N)
print(result)