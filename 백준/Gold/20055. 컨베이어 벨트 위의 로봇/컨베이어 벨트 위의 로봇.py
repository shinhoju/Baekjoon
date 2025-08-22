# 20055. 컨베이어 벨트 위의 로봇


N, K = map(int, input().split())
arr = list(map(int, input().split()))
robots = [False] * N

count = 0
while True:
    # [1] 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    # 회전한 위치가 내리는 위치면 내림
    count += 1

    n_arr = [0] * (2 * N)
    for i in range(2 * N):
        n_arr[(i + 1) % (2 * N)] = arr[i]

    n_robots = [False] * N
    for i in range(N):
        if robots[i] and i + 1 == N - 1:
            n_robots[(i + 1) % N] = False
        else:
            n_robots[(i + 1) % N] = robots[i]

    # [2] 가장 먼저 벨트에 올라간 로봇 -> 벨트가 회전하는 방향으로 한 칸 이동
    # [2-1] 이동하려는 칸에 로봇 x, 내구도 >= 1
    for i in range(N-1, -1, -1):
        if n_robots[i]:
            if i + 1 < N:
                if not n_robots[i + 1] and n_arr[i + 1] >= 1:
                    n_robots[i] = False
                    n_arr[i + 1] -= 1
                    # 내리는 위치 확인
                    if i + 1 != N - 1:
                        n_robots[i + 1] = True

    # [3] 올리는 칸에 로봇 올림
    if n_arr[0] > 0:
        n_arr[0] -= 1
        n_robots[0] = True

    # [4] 내구도가 0인 칸의 개수가 K 개 이상이면 종료
    zeros = 0
    for i in range(2 * N):
        if n_arr[i] == 0:
            zeros += 1
    if zeros >= K:
        break

    arr = n_arr
    robots = n_robots

print(count)
