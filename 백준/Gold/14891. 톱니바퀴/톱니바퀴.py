# 14891. 톱니바퀴
from collections import deque

# 0: N극, 1: S극
arr = []
for _ in range(4):
    # temp = list(input().split())
    temp = list(map(int, input()))
    arr.append(temp)


# 1: 시계, -1: 반시계
K = int(input())
move = []
for _ in range(K):
    move.append(list(map(int, input().split())))


def bfs(n, dr):
    global v

    q = deque()
    q.append((n, dr))

    while q:
        n, dr = q.popleft()

        # 왼쪽 확인
        ln = n - 1
        if ln >= 0:
            if arr[n][6] != arr[ln][2] and not v[ln]:
                q.append((ln, -dr))
                v[ln] = -dr

        # 오른쪽 확인
        rn = n + 1
        if rn <= 3:
            if arr[n][2] != arr[rn][6] and not v[rn]:
                q.append((rn, -dr))
                v[rn] = -dr
    return


# start
for num, d in move:
    # [1] 회전할 톱니바퀴 찾기
    num = num - 1

    v = [0] * 4
    v[num] = d
    bfs(num, d)

    # [2] 회전
    for num, d in enumerate(v):
        if not d:
            continue

        temp = [0] * 8
        for idx, x in enumerate(arr[num]):
            if d == 1:
                temp[(idx+1)%8] = x
            else:
                temp[(idx-1)%8] = x

        arr[num] = temp

# [3] 최종 상태
result = 0
for idx in range(4):
    if arr[idx][0] == 1:
        result += pow(2, idx)

print(result)