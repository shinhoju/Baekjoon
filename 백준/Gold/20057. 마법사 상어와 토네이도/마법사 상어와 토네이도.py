# 20057. 마법사 상어와 토네이도

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
tx, ty, td, tl = N // 2, N // 2, 0, 1          # 토네이도 위치 좌표, 방향

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

mul = [2, 10, 7, 1, 5, 10, 7, 1, 2, 0]
ax = [[-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0],
      [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]]

ay = [[0, -1, 0, 1, -2, -1, 0, 1, 0, -1],
      [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0]]


cur_l = answer = 0               # 현재 변의 길이
flag = False            # 변의 길이 증가 할 말
while (tx, ty) != (0, 0):
    tx, ty = tx + dx[td], ty + dy[td]

    if arr[tx][ty] > 0:
        # 모래 날리기
        tsand = arr[tx][ty]
        arr[tx][ty] = sum_s = 0     # sum_s: 날라간 모래 총 합

        for i in range(10):
            nx, ny = tx + ax[td][i], ty + ay[td][i]
            s = (tsand * mul[i]) // 100
            if i == 9:
                s = tsand - sum_s

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                answer += s
            else:
                arr[nx][ny] += s
            sum_s += s

    cur_l += 1
    if cur_l == tl:
        td = (td + 1) % 4
        cur_l = 0
        if not flag:            # 길이 증가 x
            flag = True
        else:                   # 길이 증가 o
            flag = False
            tl += 1

print(answer)
