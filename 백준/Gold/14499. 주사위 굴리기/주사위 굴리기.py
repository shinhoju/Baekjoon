N, M, x, y, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
move = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice_arr = [0, 0, 0, 0, 0, 0]
dice = [0, 2, 4]
opp = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}


def roll_dice(lst, num):
    n_lst = [0] * 3
    if num == 1:
        n_lst[0] = lst[1]
        n_lst[1] = opp[lst[0]]
        n_lst[2] = lst[2]
        return n_lst
    elif num == 2:
        n_lst[0] = opp[lst[1]]
        n_lst[1] = lst[0]
        n_lst[2] = lst[2]
    elif num == 3:
        n_lst[0] = opp[lst[2]]
        n_lst[1] = lst[1]
        n_lst[2] = lst[0]
    elif num == 4:
        n_lst[0] = lst[2]
        n_lst[1] = lst[1]
        n_lst[2] = opp[lst[0]]
    return n_lst


def in_range(r, c):
    if r < 0 or r >= N or c < 0 or c >= M:
        return False
    else:
        return True


for d in move:
    # 주사위 다음 위치: 맵 바깥 x, 무시
    nx, ny = x + dx[d], y + dy[d]
    if not in_range(nx, ny):
        continue

    # d 방향 주사위 굴리기 -> dice 변화
    # 이동한 칸에 쓰여 있는 수 0 => 주사위 바닥 수 복사
    # 이동한 칸에 쓰여 있는 수 0이 아닌 경우 => 주사위 바닥 면으로 복사, 칸 0
    n_dice = roll_dice(dice, d)
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice_arr[n_dice[0]]
    elif arr[nx][ny] > 0:
        dice_arr[n_dice[0]] = arr[nx][ny]
        arr[nx][ny] = 0

    # 상단에 쓰여 있는 값 구하기
    print(dice_arr[opp[n_dice[0]]])
    x, y = nx, ny
    dice = n_dice