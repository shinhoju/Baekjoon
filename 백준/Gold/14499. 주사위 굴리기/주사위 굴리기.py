N, M, x, y, K = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))
move = list(map(int, input().split()))

# 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice_map = [0] * 6

d_center = 0
d_left = 1
d_bottom = 2

def roll_dice(d):
    global d_center, d_left, d_bottom

    c_temp = d_center
    l_temp = d_left
    b_temp = d_bottom

    if d == 1:
        # 동쪽
        d_center = l_temp
        d_left = (c_temp + 3) % 6
        d_bottom = b_temp

    if d == 2:
        # 서쪽
        d_center = (l_temp + 3) % 6
        d_left = c_temp
        d_bottom = b_temp

    if d == 3:
        # 북쪽
        d_center = (b_temp + 3) % 6
        d_left = l_temp
        d_bottom = c_temp

    if d == 4:
        # 남쪽
        d_center = b_temp
        d_left = l_temp
        d_bottom = (c_temp + 3) % 6


for m in move:
    nx, ny = x + dx[m], y + dy[m]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    roll_dice(m)

    if maps[nx][ny] == 0:
        maps[nx][ny] = dice_map[d_center]
    else:
        dice_map[d_center] = maps[nx][ny]
        maps[nx][ny] = 0

    x, y = nx, ny
    print(dice_map[(d_center + 3) % 6])