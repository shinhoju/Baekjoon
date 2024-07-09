from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)
result1 = []
result2 = []

# dfs
def dfs(x):
    visited1[x] = True
    result1.append(x)
    graph[x].sort()

    for i in graph[x]:
        if not visited1[i]:
            dfs(i)

def bfs(x):
    queue = deque()
    queue.append(x)
    visited2[x] = True

    while queue:
        x = queue.popleft()
        graph[x].sort()
        result2.append(x)

        for i in graph[x]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True


dfs(V)
bfs(V)
print(*result1)
print(*result2)