# 19237. 어른 상어

N, M, K = map(int, input().split())
temp = []
for _ in range(N):
    temp.append(list(map(int, input().split())))
temp_2 = list(map(int, input().split()))
sharks = {}
for i in range(N):
    for j in range(N):
        if temp[i][j] > 0:
            sharks[temp[i][j]] = [i, j, temp_2[temp[i][j]-1]]

priority = {}
for i in range(M * 4):
    if not (i // 4 + 1) in priority.keys():
        priority[i // 4 + 1] = [list(map(int, input().split()))]
    else:
        priority[i // 4 + 1].append(list(map(int, input().split())))
arr = [[[0, 0] for _ in range(N)] for _ in range(N)]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


def in_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True


# [1] 상어 init
for s_num, [si, sj, sd] in sharks.items():
    arr[si][sj] = [s_num, K]
ans = 0
while True:
    # 종료 조건: 상어가 1마리만 남음
    if len(sharks) == 1:
        break
    if ans >= 1000:
        ans = -1
        break

    # [2] 상어 방향 정하기
    # [2-1] 아무 냄새 없는 칸의 방향 -> 자기 냄새 있는 방향
    for s_num, [si, sj, sd] in sharks.items():
        n_si, n_sj, n_sd = 30, 30, 5
        for pd in priority[s_num][sd-1]:
            ni, nj = si + dx[pd], sj + dy[pd]
            if not in_range(ni, nj):
                continue
            if arr[ni][nj] == [0, 0]:
                n_si, n_sj, n_sd = ni, nj, pd
                break
        if n_sd == 5:
            for pd in priority[s_num][sd-1]:
                ni, nj = si + dx[pd], sj + dy[pd]
                if not in_range(ni, nj):
                    continue
                if arr[ni][nj][0] == s_num:
                    n_si, n_sj, n_sd = ni, nj, pd
                    break
        sharks[s_num] = [n_si, n_sj, n_sd]

    # [4] 냄새 - 1
    for i in range(N):
        for j in range(N):
            if arr[i][j][1] > 1:
                arr[i][j][1] -= 1
            elif arr[i][j][1] == 1:
                arr[i][j] = [0, 0]


    # [3] 같은 위치에 있는 상어 검사
    temp = []
    for i in range(1, M+1):
        if i in sharks.keys():
            si, sj, _ = sharks[i]
            if (si, sj) in temp:
                sharks.pop(i)
            else:
                arr[si][sj] = [i, K]
                temp.append((si, sj))

    ans += 1

print(ans)
