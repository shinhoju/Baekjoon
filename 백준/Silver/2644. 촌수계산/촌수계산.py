# 사람 수
N = int(input())

# 구해야 되는 관계
S, T = map(int, input().split())

# 부모-자식 관계 수
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
results = []

def dfs(v, num):
    visited[v] = True

    if v == T:
        results.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num + 1)

dfs(S, 0)
if len(results) == 0:
    print(-1)
else:
    print(*results)