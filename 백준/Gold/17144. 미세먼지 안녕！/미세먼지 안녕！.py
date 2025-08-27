# 17144. 미세먼지 안녕!

R, C, T = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(map(int, input().split())))
robots = []
robots_d = [0, 0]
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            robots.append((i, j))
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def in_range(x, y):
    if x < 0 or x >= R or y < 0 or y >= C:
        return False
    else:
        return True


# wind(robots[0], 1)          # 시계 방향 회전
def wind(x, y, s):
    tmp = [a[:] for a in arr]
    cx, cy, cd = x + dx[0], y + dy[0], 0
    tmp[cx][cy] = 0
    while True:
        nx, ny = cx + dx[cd], cy + dy[cd]
        if (nx, ny) == (x, y):
            break
        # 다음 위치 범위 벗어남 -> 방향 전환, 새로운 위치 찾기
        if not in_range(nx, ny):
            cd = (cd + s) % 4
            nx, ny = cx + dx[cd], cy + dy[cd]
        tmp[nx][ny] = arr[cx][cy]
        cx, cy = nx, ny
    return tmp


for _ in range(T):
    # [1] 미세 먼지 확산
    n_arr = [a[:] for a in arr]
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5:
                tmp = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if not in_range(ni, nj):
                        continue
                    if not arr[ni][nj] == -1:
                        n_arr[ni][nj] += arr[i][j] // 5
                        tmp += 1
                n_arr[i][j] = n_arr[i][j] - tmp * (arr[i][j] // 5)
    arr = n_arr

    # [2] 공기 청정기 작동
    arr = wind(robots[0][0], robots[0][1], 1)          # 시계 방향 회전
    arr = wind(robots[1][0], robots[1][1], -1)         # 반시계 방향 회전

# [3] 남아있는 미세먼지의 양
result = 0
for i in range(R):
    result += sum(arr[i])
print(result+2)
