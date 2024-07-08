m = int(input())
n = int(input())

graph = [[] for _ in range(m+1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (m + 1)
result = 0

def dfs(x):
    global result
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            dfs(i)
            result += 1

dfs(1)
print(result)