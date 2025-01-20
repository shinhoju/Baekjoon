# 로봇 청소기

N, M = map(int, input().split())
x, y, d = map(int, input().split())

# 0: 빈 칸, 1: 벽, -1: 청소 완료
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def empty_space(r, c):
    flag = False        # 빈 칸이 없음
    for n in range(4):
        # 1칸 이라도 빈 칸이 있으면 flag 변경
        if table[r+dx[n]][c+dy[n]] == 0:
            flag = True
            break

    return flag


result = 0

while True:
    # [1] 현재 칸이 빈 칸인 경우, 청소
    if table[x][y] == 0:
        table[x][y] = -1
        result += 1

    # [2] 현재 칸의 주변 4칸 중 청소 안 된 빈 칸이 없는 경우
    if not empty_space(x, y):
        # [2-1] 방향 유지, 한 칸 후진, 1번으로 이동
        # [2-2] 만약 후진한 칸이 벽이면 멈춤
        nx, ny = x + dx[(d+2)%4], y + dy[(d+2)%4]
        if table[nx][ny] == 1:
            break
        else:
            x, y = nx, ny
            continue

    # [3] 현재 칸 주변 4칸 중 청소 되지 않은 칸이 있는 경우
    else:
        # [3-1] 반시계 방향 90도 회전
        # [3-2] 방향 기준 앞쪽 칸이 청소 안 된 칸이면 한 칸 전진
        d = (d-1) % 4
        nx, ny = x + dx[d], y + dy[d]
        if table[nx][ny] == 0:
            x, y = nx, ny

print(result)