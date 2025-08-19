# 14503. 로봇청소기

N, M = map(int, input().split())
rx, ry, rd = map(int, input().split())

# 0: 빈 칸, 1: 벽, 2: 청소 완
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def empty_ck(x, y):
    flag = False

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if arr[nx][ny] == 0:            # 빈 칸 있으면 flag 수정
            flag = True

    return flag


def in_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    else:
        return True


result = 0
while True:
    # [1] 현재 칸 청소x : 현재 칸 청소
    if arr[rx][ry] == 0:
        result += 1
        arr[rx][ry] = 2

    # [2] 현재 칸의 주변 4칸 중 빈 칸 없는 경우
    if not empty_ck(rx, ry):
        # [2-1] 후진할 수 있으면 후진 -> 1번으로 돌아감
        # [2-2] 후진할 수 없으면 멈춤
        nx, ny = rx + dx[(rd + 2) % 4], ry + dy[(rd + 2) % 4]
        if not in_range(nx, ny):
            break
        if arr[nx][ny] == 1:
            break
        else:
            rx, ry = nx, ny
            continue
    # [3] 현재 칸의 주변 4칸 중 빈 칸 있는 경우
    else:
        # [3-1] 반시계 90도 회전
        for i in range(1, 5):
            nrd = (rd - i) % 4
            nx, ny = rx + dx[nrd], ry + dy[nrd]
            if in_range(nx, ny):
                if arr[nx][ny] == 0:
                    rx, ry = nx, ny
                    rd = nrd
                    break

print(result)