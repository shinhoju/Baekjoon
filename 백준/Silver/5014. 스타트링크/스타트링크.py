from collections import deque

# 건물 총 높이, 현재 위치, 목표 위치, 위로 몇 칸, 아래로 몇 칸
F, S, G, U, D = map(int, input().split())

maps = [0] * (F + 1)

def bfs(x):
    queue = deque()
    queue.append(x)
    maps[x] += 1

    while queue:
        x = queue.popleft()

        if x == G:
            return maps[G] - 1

        for nx in (x+U, x-D):
            if nx <= 0 or nx > F:
                continue
            if not maps[nx]:
                queue.append(nx)
                maps[nx] = maps[x] + 1
    else:
        return "use the stairs"


print(bfs(S))