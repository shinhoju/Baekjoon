# 20056. 마법사 상어와 파이어볼

N, M, K = map(int, input().split())
balls = {}
for _ in range(M):
    # r, c, m, s, d: 위치 / 질량 / 속력 / 방향
    r, c, m, s, d = map(int, input().split())
    balls[(r, c)] = [[m, s, d]]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def direction(arr):
    cur_d = arr[0]
    flag = False
    for next_d in arr[1:]:
        if cur_d != next_d:
            flag = True
    return flag


for _ in range(K):
    # [1] 모든 파이어 볼 이동
    new_balls = {}
    for (r, c) in balls.keys():
        for m, s, d in balls[(r, c)]:
            nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
            if not (nr, nc) in new_balls.keys():
                new_balls[(nr, nc)] = [[m, s, d]]
            else:
                new_balls[(nr, nc)].append([m, s, d])

    # [2] 이동이 끝난 후, 2개 이상의 파이어 볼이 있는 칸
    remove = []
    for (r, c) in new_balls.keys():
        if len(new_balls[(r, c)]) > 1:
            new_m = 0
            new_s = 0
            new_ds = []
            for m, s, d in new_balls[(r, c)]:
                new_s += s
                new_m += m
                new_ds.append(d % 2)
            new_m = new_m // 5
            new_s = new_s // len(new_balls[(r, c)])
            new_ds = [1, 3, 5, 7] if direction(new_ds) else [0, 2, 4, 6]
            if new_m > 0:
                new_balls[(r, c)] = [[new_m, new_s, new_d] for new_d in new_ds]
            else:
                remove.append((r, c))
    for key in remove:
        new_balls.pop(key)
    balls = new_balls

result = 0
for ball in balls.values():
    for m, _, _ in ball:
        result += m

print(result)