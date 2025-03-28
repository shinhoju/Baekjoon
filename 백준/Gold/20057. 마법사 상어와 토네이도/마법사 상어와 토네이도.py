# 20057. 마법사 상어와 토네이도

N = int(input())
sand = []
for _ in range(N):
    sand.append(list(map(int, input().split())))

# 왼 아 오 위
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 토네이도 위치 좌표, 방향
x, y = (N-1) // 2, (N-1) // 2
d = 0

schedule = []
for i in range(1, N+1):
    schedule.append(i)
    schedule.append(i)

count_s = 0
temp_s = 0

# 밖으로 나간 모래 수
result = 0


def in_range(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    else:
        return True


def tornado(r, c, direction):
    global sand, nx, ny
    out_sand = 0
    spread_sand = 0

    if direction == 0:
        # 왼쪽 날리기
        if in_range(x - 1, y):
            sand[x - 1][y] += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)
        else:
            out_sand += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)

        if in_range(x + 1, y):
            sand[x + 1][y] += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)
        else:
            out_sand += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)

        if in_range(x - 1, y - 1):
            sand[x - 1][y - 1] += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)
        else:
            out_sand += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)

        if in_range(x + 1, y - 1):
            sand[x + 1][y - 1] += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)
        else:
            out_sand += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)

        if in_range(x - 2, y - 1):
            sand[x - 2][y - 1] += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)
        else:
            out_sand += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)

        if in_range(x + 2, y - 1):
            sand[x + 2][y - 1] += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)
        else:
            out_sand += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)

        if in_range(x - 1, y - 2):
            sand[x - 1][y - 2] += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)
        else:
            out_sand += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)

        if in_range(x + 1, y - 2):
            sand[x + 1][y - 2] += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)
        else:
            out_sand += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)

        if in_range(x, y - 3):
            sand[x][y - 3] += int(sand[nx][ny] * 0.05)
            spread_sand += int(sand[nx][ny] * 0.05)
        else:
            out_sand += int(sand[nx][ny] * 0.05)
            spread_sand += int(sand[nx][ny] * 0.05)

        if in_range(x, y - 2):
            sand[x][y - 2] += (sand[nx][ny] - spread_sand)
        else:
            out_sand += (sand[nx][ny] - spread_sand)

        return out_sand


    if direction == 1:
        # 왼쪽 날리기
        if in_range(x, y-1):
            sand[x][y-1] += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)
        else:
            out_sand += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)

        if in_range(x, y+1):
            sand[x][y+1] += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)
        else:
            out_sand += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)

        if in_range(x+1, y-1):
            sand[x + 1][y - 1] += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)
        else:
            out_sand += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)

        if in_range(x+1, y+1):
            sand[x + 1][y + 1] += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)
        else:
            out_sand += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)

        if in_range(x+1, y-2):
            sand[x + 1][y - 2] += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)
        else:
            out_sand += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)

        if in_range(x+1, y +2):
            sand[x + 1][y +2] += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)
        else:
            out_sand += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)

        if in_range(x +2, y - 1):
            sand[x +2][y - 1] += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)
        else:
            out_sand += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)

        if in_range(x + 2, y +1):
            sand[x + 2][y+1] += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)
        else:
            out_sand += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)

        if in_range(x+3, y):
            sand[x+3][y] += int(sand[nx][ny] * 0.05)
            spread_sand += int(sand[nx][ny] * 0.05)
        else:
            out_sand += int(sand[nx][ny] * 0.05)
            spread_sand += int(sand[nx][ny] * 0.05)

        if in_range(x+2, y):
            sand[x+2][y] += (sand[nx][ny] - spread_sand)
        else:
            out_sand += (sand[nx][ny] - spread_sand)

        return out_sand


    if direction == 2:
        # 왼쪽 날리기
        if in_range(x - 1, y):
            sand[x - 1][y] += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)
        else:
            out_sand += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)

        if in_range(x + 1, y):
            sand[x + 1][y] += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)
        else:
            out_sand += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)

        if in_range(x - 1, y + 1):
            sand[x - 1][y + 1] += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)
        else:
            out_sand += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)

        if in_range(x + 1, y + 1):
            sand[x + 1][y + 1] += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)
        else:
            out_sand += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)

        if in_range(x - 2, y + 1):
            sand[x - 2][y + 1] += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)
        else:
            out_sand += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)

        if in_range(x + 2, y + 1):
            sand[x + 2][y + 1] += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)
        else:
            out_sand += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)

        if in_range(x - 1, y + 2):
            sand[x - 1][y + 2] += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)
        else:
            out_sand += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)

        if in_range(x + 1, y + 2):
            sand[x + 1][y + 2] += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)
        else:
            out_sand += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)

        if in_range(x, y + 3):
            sand[x][y + 3] += int(sand[nx][ny] * 0.05)
            spread_sand += int(sand[nx][ny] * 0.05)
        else:
            out_sand += int(sand[nx][ny] * 0.05)
            spread_sand += int(sand[nx][ny] * 0.05)

        if in_range(x, y + 2):
            sand[x][y + 2] += (sand[nx][ny] - spread_sand)
        else:
            out_sand += (sand[nx][ny] - spread_sand)

        return out_sand


    if direction == 3:
        # 왼쪽 날리기
        if in_range(x, y-1):
            sand[x][y-1] += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)
        else:
            out_sand += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)

        if in_range(x, y+1):
            sand[x][y+1] += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)
        else:
            out_sand += int(sand[nx][ny] * 0.01)
            spread_sand += int(sand[nx][ny] * 0.01)

        if in_range(x-1, y-1):
            sand[x - 1][y - 1] += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)
        else:
            out_sand += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)

        if in_range(x-1, y+1):
            sand[x - 1][y + 1] += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)
        else:
            out_sand += int(sand[nx][ny] * 0.07)
            spread_sand += int(sand[nx][ny] * 0.07)

        if in_range(x-1, y-2):
            sand[x - 1][y - 2] += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)
        else:
            out_sand += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)

        if in_range(x-1, y +2):
            sand[x -1][y +2] += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)
        else:
            out_sand += int(sand[nx][ny] * 0.02)
            spread_sand += int(sand[nx][ny] * 0.02)

        if in_range(x -2, y - 1):
            sand[x -2][y - 1] += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)
        else:
            out_sand += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)

        if in_range(x - 2, y +1):
            sand[x - 2][y+1] += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)
        else:
            out_sand += int(sand[nx][ny] * 0.1)
            spread_sand += int(sand[nx][ny] * 0.1)

        if in_range(x-3, y):
            sand[x-3][y] += int(sand[nx][ny] * 0.05)
            spread_sand += int(sand[nx][ny] * 0.05)
        else:
            out_sand += int(sand[nx][ny] * 0.05)
            spread_sand += int(sand[nx][ny] * 0.05)

        if in_range(x-2, y):
            sand[x-2][y] += (sand[nx][ny] - spread_sand)
        else:
            out_sand += (sand[nx][ny] - spread_sand)

        return out_sand



while True:
    if (x, y) == (0, 0):
        break

    nx, ny = x + dx[d], y + dy[d]

    # 모래 날리기
    if sand[nx][ny] > 0:
        temp = tornado(x, y, d)
        result += temp

    # 회전 코드
    temp_s += 1
    if temp_s == schedule[count_s]:
        d = (d + 1) % 4
        temp_s = 0
        count_s += 1

    x, y = nx, ny

print(result)