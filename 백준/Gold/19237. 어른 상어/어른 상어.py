# 19237. 어른 상어
from copy import deepcopy

N, M, k = map(int, input().split())
sharks = dict()
for r in range(N):
    for c, v in enumerate(list(map(int, input().split()))):
        if v > 0:
            sharks[v] = (r, c)

sharks = dict(sorted(sharks.items()))

sharks_d = [0]
for s in list(map(int, input().split())):
    sharks_d.append(s)

priority = dict()
for i in range(M*4):
    temp = list(map(int, input().split()))
    temp2 = {1: temp.index(1)+1, 2: temp.index(2)+1, 3: temp.index(3)+1, 4:temp.index(4)+1}
    if i//4+1 in priority.keys():
        priority[i//4+1].append(temp2)
    else:
        priority[i//4+1] = [temp2]

# 1: 위, 2: 아래, 3: 왼쪽, 4: 오른쪽
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


# 1번 상어만 남게 될 떄 까지 카운트
count = 0
ocean = [[[0, 0]] * N for _ in range(N)]
while True:
    if len(sharks) == 1:
        break

    count += 1

    if count > 1000:
        count = -1
        break


    # [1] 자신의 위치에 냄새 뿌림
    for n, (x, y) in sharks.items():
        ocean[x][y] = [n, k]

    check = [[[0] for _ in range(N)] for _ in range(N)]

    # [2] 상어 이동
    # [2-1] 인접한 칸 중 아무 냄새가 없는 칸의 방향 / 자기 냄새 칸 방향
    n_sharks = deepcopy(sharks)
    for n, (x, y) in sharks.items():
        psb_no_d = []
        psb_same_d = []
        for i in range(1,5):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if ocean[nx][ny] == [0, 0]:
                psb_no_d.append(i)
            elif ocean[nx][ny][0] == n:
                psb_same_d.append(i)

        # [2-2] 아무 냄새 x 칸 ) 한 개일 때, 여러 개일 때
        if len(psb_no_d) >= 1:
            if len(psb_no_d) > 1:
                psb_no_d.sort(key=lambda v: priority[n][sharks_d[n] - 1][v])
            sharks_d[n] = psb_no_d[0]
            n_sharks[n] = (x + dx[psb_no_d[0]], y + dy[psb_no_d[0]])
            check[n_sharks[n][0]][n_sharks[n][1]].append(n)

        # [2-3] 자기 냄새 칸 ) 한 개일 때, 여러 개일 때
        else:
            if len(psb_same_d) > 1:
                psb_same_d.sort(key=lambda v: priority[n][sharks_d[n] - 1][v])
            sharks_d[n] = psb_same_d[0]
            n_sharks[n] = (x + dx[psb_same_d[0]], y + dy[psb_same_d[0]])
            check[n_sharks[n][0]][n_sharks[n][1]].append(n)
    sharks = n_sharks

    # [3] 냄새 - 1
    for i in range(N):
        for j in range(N):
            if ocean[i][j][1] > 1:
                ocean[i][j][1] -= 1
            elif ocean[i][j][1] == 1:
                ocean[i][j] = [0, 0]

    # [4] 한 칸에 여러 마리 남아 있으면, 가장 작은 번호 상어만 남기고 나감
    for i in range(N):
        for j in range(N):
            if len(check[i][j]) > 2:
                check[i][j].sort()
                # 젤 작은 번호 빼고 다 나가
                check[i][j].pop(0)
                check[i][j].pop(0)
                non_exist_num = check[i][j]
                for num in non_exist_num:
                    sharks.pop(num)

print(count)