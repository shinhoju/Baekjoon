# 마법사 상어와 비바라기
# 구현, 시뮬레이션

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

move = []
for _ in range(M):
    move.append(list(map(int, input().split())))

# 1번 부터 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 구름 위치 저장
cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

for d, s in move:
    # [1] 모든 구름 이동
    new_cloud = []
    for cx, cy in cloud:
        # 행, 열 연결 되어 있음
        ncx, ncy = cx + s * dx[d], cy + s * dy[d]
        if ncx < 0:
            ncx = N - (abs(ncx) % N)
        if ncx >= N:
            ncx = ncx % N
        if ncy < 0:
            ncy = N - (abs(ncy) % N)
        if ncy >= N:
            ncy = ncy % N
        new_cloud.append((ncx, ncy))
        # [2] 비가 내려 구름이 있는 칸 바구니 저장된 물의 양 + 1
        A[ncx][ncy] += 1

    # [4] 물 복사 버그: new_cloud 칸에서 대각선 검사, 연결된 칸 x
    for cx, cy in new_cloud:
        bug = 0
        for n in [2, 4, 6, 8]:
            ncx, ncy = cx + dx[n], cy + dy[n]
            if ncx < 0 or ncx >= N or ncy < 0 or ncy >= N:
                continue
            if A[ncx][ncy] > 0:
                bug += 1
        A[cx][cy] += bug

    # [5] 바구니 물 2 이상인 칸에 구름이 생기고 물의 양 -2, cloud 저장된 칸 x
    next_cloud = []
    for i in range(N):
        for j in range(N):
            if (i, j) in new_cloud:
                continue
            if A[i][j] >= 2:
                next_cloud.append((i, j))
                A[i][j] -= 2

    cloud = next_cloud

result = 0
for i in range(N):
    for j in range(N):
        result += A[i][j]

print(result)