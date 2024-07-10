N = int(input())
graph = []
num = []

for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

cnt = 0
result = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            num.append(cnt)
            result += 1
            cnt = 0

print(result)
num.sort()
for i in range(len(num)):
    print(num[i])