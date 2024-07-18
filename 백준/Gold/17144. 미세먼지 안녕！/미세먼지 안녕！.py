R, C, T = map(int, input().split())
room = []
for _ in range(R):
    room.append(list(map(int, input().split())))

# 우 상 좌 하 / 우 하 좌 상
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

def air_fresh(flag, ai, aj, ad):
    global temp, room, air
    if not flag:
        ni, nj = ai + di[ad], aj + dj[ad]

        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            ad = (ad + 1) % 4
            ni, nj = ai + di[ad], aj + dj[ad]

        if not (ni, nj) == (air[flag][0], air[flag][1]):
            temp[ni][nj] = room[ai][aj]
            air_fresh(flag, ni, nj, ad)
        else:
            room = temp
            return
    else:
        ni, nj = ai + di[ad], aj + dj[ad]

        if ni < 0 or ni >= R or nj < 0 or nj >= C:
            ad = (ad - 1) % 4
            ni, nj = ai + di[ad], aj + dj[ad]

        if not (ni, nj) == (air[flag][0], air[flag][1]):
            temp[ni][nj] = room[ai][aj]
            air_fresh(flag, ni, nj, ad)
        else:
            room = temp
            return

for _ in range(T):
    air = []
    temp = [r[:] for r in room]
    # [1] 미세 먼지 확산
    for i in range(R):
        for j in range(C):
            if room[i][j] >= 1:
                cnt = 0
                for n in range(4):
                    ni, nj = i + di[n], j + dj[n]
                    if ni < 0 or ni >= R or nj < 0 or nj >= C:
                        continue
                    if room[ni][nj] >= 0:
                        temp[ni][nj] += room[i][j] // 5
                        cnt += 1
                if cnt:
                    temp[i][j] -= (room[i][j] // 5) * cnt
            elif room[i][j] == -1:
                air.append((i, j))
    room = temp

    # [2] 공기 청정기 작동
    for i, (ai, aj) in enumerate(air):
        aj += 1
        ad = 0
        temp = [r[:] for r in room]
        temp[ai][aj] = 0
        air_fresh(i, ai, aj, ad)

# 결과 출력
result = 2
for r in room:
    result += sum(r)

print(result)