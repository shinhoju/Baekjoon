N, K = map(int, input().split())
belt = list(map(int, input().split()))

result = 0
zeros = 0
robots = [False] * (2 * N)

while True:
    result += 1

    # [1] 벨트 로봇 회전
    n_belt = [0] * (2 * N)
    for i in range(2 * N):
        n_belt[i] = belt[i - 1]
    belt = n_belt

    n_robots = [False] * (2 * N)
    for i in range(2 * N):
        if robots[i]:
            if (i + 1) != (N - 1):
                n_robots[(i + 1) % (2 * N)] = True
    robots = n_robots

    # [2] 로봇 스스로 이동
    n_robots = [r for r in robots]
    for i in range(N-1, -1, -1):
        if robots[i]:
            if not n_robots[i + 1] and belt[i + 1] >= 1:
                if (i + 1) != (N - 1):
                    n_robots[i + 1] = True
                n_robots[i] = False
                belt[i + 1] -= 1
                if belt[i + 1] == 0:
                    zeros += 1
            else:
                n_robots[i] = True
    robots = n_robots

    # [3] 로봇 올리기
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            zeros += 1

     # [4] 내구도 0인 칸 K개 이상이면 종료
    if zeros >= K:
        break

print(result)