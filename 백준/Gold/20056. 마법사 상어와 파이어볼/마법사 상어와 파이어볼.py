# 20056. 마법사 상어와 파이어 볼

from copy import deepcopy

N, M, K = map(int, input().split())
fire = dict()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire[(r, c)] = [[m, s, d]]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # [1] 모든 파이어 볼이 d 방향, s칸 만큼 이동
    new_fire = {}
    for ri, ci in fire.keys():
        for mi, si, di in fire[(ri, ci)]:
            nr = (ri + dx[di] * si) % N
            nc = (ci + dy[di] * si) % N

            if (nr, nc) in new_fire.keys():
                new_fire[(nr, nc)].append([mi, si, di])
            else:
                new_fire[(nr, nc)] = [[mi, si, di]]
    fire = new_fire

    # [2] 이동이 끝난 후, 2개 이상의 파이어 볼이 있는 칸
    new_fire = deepcopy(fire)
    for ri, ci in fire.keys():
        if len(fire[(ri, ci)]) >= 2:
            sum_m = 0
            sum_s = 0
            sum_d = []
            for mi, si, di in fire[(ri, ci)]:
                sum_m += mi
                sum_s += si
                sum_d.append(0 if di % 2 == 0 else 1)

            new_m = sum_m // 5
            new_s = sum_s // len(fire[(ri, ci)])

            if new_m == 0:
                new_fire.pop((ri, ci))
            else:
                if all(num % 2 == 0 for num in sum_d) or all(num % 2 == 1 for num in sum_d):
                    new_fire[(ri, ci)] = [[new_m, new_s, 0], [new_m, new_s, 2], [new_m, new_s, 4], [new_m, new_s, 6]]
                else:
                    new_fire[(ri, ci)] = [[new_m, new_s, 1], [new_m, new_s, 3], [new_m, new_s, 5], [new_m, new_s, 7]]
    fire = new_fire


# [3] 남은 질량
result = 0
for f in fire.values():
    for m, _, _ in f:
        result += m

print(result)