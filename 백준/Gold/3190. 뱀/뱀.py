from collections import deque

N = int(input())
K = int(input())

board = [[0] * (N+2) for _ in range(N+2)]
board[1][1] = 1

apple = []
for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 2
    apple.append((x, y))

L = int(input())
# move = (시간, 방향 = L: 왼쪽 D: 오른쪽)
move = {}
for _ in range(L):
    a, b = input().split()
    move[int(a)] = b

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
# hx, hy = 1, 1       # 머리 좌표
# tx, ty = 1, 1       # 꼬리 좌표
snake = deque()
snake.append((1, 1))

cnt = 0
while True:
    cnt += 1
    # [1] 뱀 이동
    # [1-2] 머리 이동
    hx, hy = snake[0]
    hnx, hny = hx + dx[d], hy + dy[d]
    # 종료 조건
    if hnx <= 0 or hnx >= N+1 or hny <= 0 or hny >= N+1:
        break
    if board[hnx][hny] == 1:
        break

    # 사과가 있을 때:
    if board[hnx][hny] == 2:
        board[hnx][hny] = 1
        snake.appendleft((hnx, hny))
    # 사과가 없을 때
    else:
        tx, ty = snake.pop()
        board[tx][ty] = 0
        board[hnx][hny] = 1
        snake.appendleft((hnx, hny))

    # [1-1] 방향 바꾸어야 할 때
    if cnt in move.keys():
        md = move[cnt]
        if md == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4

print(cnt)