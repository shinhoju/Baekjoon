N, M = map(int, input().split())

# 바구니 내부의 물 저장
water = []
for _ in range(N):
    water.append(list(map(int, input().split())))

move = []
for _ in range(M):
    move.append(list(map(int, input().split())))

# 좌 좌상 상 우상 우 우하 하 좌하 (대각선: 1, 3, 5, 7)
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 초기 상태 구름
cloud = [[0] * N for _ in range(N)]
cloud[N-2][0] = 1
cloud[N-1][0] = 1
cloud[N-2][1] = 1
cloud[N-1][1] = 1

def move_cloud(md, ms):
    global cloud
    temp = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if cloud[r][c] == 1:
                # 이동, 위 아래 및 양 옆 연결 되어 있음
                nr, nc = (r + dr[md]*ms + N) % N, (c + dc[md]*ms + N) % N
                cloud[r][c] = 0
                temp[nr][nc] = 1
    cloud = temp


for md, ms in move:
    # [1] 구름 이동 (방향, 거리)
    move_cloud(md-1, ms)

    # [3] 구름 없애기
    new_cloud = [[0] * N for _ in range(N)]

    # [2] 비 내리기 (바구니 +1)
    # [4] 물이 증가한 곳 (구름 존재 했던 위치) 물복사 버그 마법 사용
    # [5] 바구니 저장된 물의 양이 2 이상인 칸에 구름 생기고, 물 - 2
    #     구름이 사라진 칸이 x

    for r in range(N):
        for c in range(N):
            if cloud[r][c] == 1:
                # [2]
                water[r][c] += 1

    for r in range(N):
        for c in range(N):
            if cloud[r][c] == 1:
                for i in range(1, 8, 2):
                    nr, nc = r + dr[i], c + dc[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    if water[nr][nc] >= 1:
                        water[r][c] += 1

    # [4] 물이 증가한 곳 (구름 존재 했던 위치) 물복사 버그 마법 사용
    # for r in range(N):
    #     for c in range(N):
    #         if cloud[r][c] == 1:
    #             # 대각선 방향 물이 있는지 확인 후 물 + 1
    #             for i in range(1, 8, 2):
    #                 nr, nc = r + dr[i], c + dc[i]
    #                 if nr < 0 or nr >= N or nc < 0 or nc >= N:
    #                     continue
    #                 water[r][c] += 1

    for r in range(N):
        for c in range(N):
            # [5]
            if water[r][c] >= 2 and not cloud[r][c]:
                new_cloud[r][c] = 1
                water[r][c] -= 2

    cloud = new_cloud

result = 0
for i in range(N):
    result += sum(water[i])

print(result)