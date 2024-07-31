N, K = map(int, input().split())
durability = list(map(int, input().split()))

cnt = 0                 # 몇 번 단계를 반복 ?
zeros = 0               # 내구도 0인 칸 몇 개 ?
robot = [False] * (2 * N)

while True:
    cnt += 1
    belt = [0] * (2 * N)
    # [1] 벨트가 각 칸 위에 있는 로봇과 함께 회전
    for i in range(2 * N):
        belt[i] = durability[i - 1]
    durability = belt

    temp = [False] * (2 * N)
    for i in range(2 * N):
        if robot[i]:
            if (i + 1) != (N - 1):
                temp[(i + 1) % (2 * N)] = True
    robot = temp

    # [2] 로봇 이동
    temp = [r for r in robot]
    for i in range(N-2, -1, -1):
        if robot[i]:
            if not temp[i + 1] and durability[i + 1] >= 1:
                if (i + 1) != (N - 1):
                    temp[i + 1] = True
                temp[i] = False
                durability[i + 1] -= 1
                if durability[i + 1] == 0:
                    zeros += 1
            else:
                temp[i] = True
    robot = temp

    #[3] 로봇 올리기
    if durability[0] != 0:
        robot[0] = True
        durability[0] -= 1
        if durability[0] == 0:
            zeros += 1

    # [4] 내구도 0인 칸이 K 개 이상 --> 종료
    if zeros >= K:
        break

print(cnt)