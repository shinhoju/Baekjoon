# 21610. 마법사 상어와 비바라기

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
move = []
for _ in range(M):
    t1, t2 = map(int, input().split())
    move.append((t1-1, t2))
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for d, s in move:
    # [1] 모든 구름 이동
    # [2] 구름이 있는 위치 -> 바구니 + 1
    next_cloud = []
    for cx, cy in cloud:
        ncx, ncy = (cx + s * dx[d]) % N, (cy + s * dy[d]) % N
        next_cloud.append((ncx, ncy))
        arr[ncx][ncy] += 1

    # [3] 물이 증가한 칸에 마법 -> 대각선 방향 거리 1인 칸에 물 존재 바구니 수 만큼 물 증가
    # 물이 증가한 칸 = 새로운 구름 위치
    for cx, cy in next_cloud:
        basket = 0
        for dr in range(1, 8, 2):
            ncx, ncy = cx + dx[dr], cy + dy[dr]
            if ncx < 0 or ncx >= N or ncy < 0 or ncy >= N:
                continue
            if arr[ncx][ncy] > 0:
                basket += 1
        arr[cx][cy] += basket

    # [4] 물의 양 2 이상인 칸에 구름 생김 -> 물의 양 - 2
    # 3에서 사라진 구름 칸이 아니어야 함
    cloud = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not (i, j) in next_cloud:
                cloud.append((i, j))
                arr[i][j] -= 2

# 바구니에 들어있는 물의 합
result = 0
for i in range(N):
    for j in range(N):
        result += arr[i][j]

print(result)