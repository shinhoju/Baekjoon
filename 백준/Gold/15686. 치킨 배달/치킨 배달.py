from itertools import combinations

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            chicken.append((i, j))
        elif maps[i][j] == 1:
            house.append((i, j))

graph = {}
for hx, hy in house:
    graph[(hx, hy)] = []
    for cx, cy in chicken:
        temp = (abs(hx - cx)) + (abs(hy - cy))
        graph[(hx, hy)].append(temp)


temp = 0
if len(chicken) <= M:
    dist = []
    temp = 0
    for h in graph.values():
        temp += min(h)
    dist.append(temp)

else:
    dist = []
    for comb in combinations(range(len(chicken)), M):
        temp = 0
        for h in graph.values():
            min_dist = min(h[i] for i in comb)
            temp += min_dist
        dist.append(temp)

print(min(dist))