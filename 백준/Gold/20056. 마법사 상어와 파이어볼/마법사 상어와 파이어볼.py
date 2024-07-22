from copy import deepcopy

N, M, K = map(int, input().split())
fire = {}
# x, y, m, s, d (위치 / 무게 / 거리 / 방향)
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    fire[(x, y)] = [(m, s, d)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # [1] 파이어 볼 이동
    nfire = {}
    next_coord = {}
    for (x, y), item in fire.items():
        for m, s, d in item:
            nx = (x + dx[d] * s + N) % N
            ny = (y + dy[d] * s + N) % N

            if (nx, ny) in nfire.keys():
                nfire[(nx, ny)].append((m, s, d))
            else:
                nfire[(nx, ny)] = [(m, s, d)]

    temp = deepcopy(nfire)

    for (x, y), item in nfire.items():
        if len(item) >= 2:
            sm = 0
            ss = 0
            sd = []

            for m, s, d in item:
                sm += m
                ss += s
                sd.append(d)

            dm = sm // 5
            ds = ss // len(item)

            if all(ddd % 2 == 0 for ddd in sd):
                dd = [0, 2, 4, 6]
            elif all(ddd % 2 == 1 for ddd in sd):
                dd = [0, 2, 4, 6]
            else:
                dd = [1, 3, 5, 7]

            tmp = []

            if not dm:
                temp.pop((x, y))
            else:
                for ddd in dd:
                    tmp.append((dm, ds, ddd))
                temp[(x, y)] = tmp

    fire = temp


result = 0
for lst in fire.values():
    for m, _, _ in lst:
        result += m

print(result)