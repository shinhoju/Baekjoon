N, M = map(int, input().split())
robot_x, robot_y, robot_d = map(int, input().split())

# 0: 청소 안된 칸 / 1: 벽 / 2: 청소한 칸
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def in_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    else:
        return True


cnt = 0
while True:
    # [1] 현재 칸 청소 안됐을 때, 청소
    if board[robot_x][robot_y] == 0:
        board[robot_x][robot_y] = 2
        cnt += 1

    # [2-1] 현재 칸의 주변 4칸 중 청소 되지 않은 빈 칸이 없는 경우
    flag = False        # false: 갈 수 없음 / true: 갈 수 있음
    for i in range(4):
        nx, ny = robot_x + dx[i], robot_y + dy[i]
        if in_range(nx, ny):
            if board[nx][ny] == 0:
                flag = True

    if not flag:
        # 종료 조건: 후진 했을 때 벽인 경우
        bd = (robot_d + 2) % 4
        bx, by = robot_x + dx[bd], robot_y + dy[bd]
        if board[bx][by] == 1:
            break
        else:
            robot_x, robot_y = bx, by
            continue

    # [2-2] 청소 되지 않은 칸이 있는 경우
    else:
        # 반시계 방향 으로 90도 회전한 후, 앞에 있는 칸이 빈 칸일 경우 전진
        robot_d = (robot_d - 1) % 4
        rx, ry = robot_x + dx[robot_d], robot_y + dy[robot_d]
        if in_range(rx, ry):
            if board[rx][ry] == 0:
                robot_x, robot_y = rx, ry
                continue

print(cnt)