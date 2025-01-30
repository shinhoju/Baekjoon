from collections import deque

N = int(input())

K = int(input())
apples = []
for _ in range(K):
    apples.append(tuple(map(int, input().split())))

L = int(input())
move = dict()
for _ in range(L):
    x, c = input().split()
    move[int(x)] = c

# 오른 아래 왼 위 (오른쪽 회전)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# snake: 몸 위치 좌표, snake_d: 머리 방향
snake = deque()
snake_d = 0
snake.append((1, 1))

result = 0


while True:
    if result in move.keys():
        if move[result] == 'L':
            snake_d = (snake_d + 3) % 4
        if move[result] == 'D':
            snake_d = (snake_d + 1) % 4

    # [1] 머리를 다음 칸에 위치
    head_x = snake[0][0] + dx[snake_d]
    head_y = snake[0][1] + dy[snake_d]

    # [2] 벽이나 자기 몸과 부딛히면 게임 끝
    if head_x < 1 or head_x > N or head_y < 1 or head_y > N:
        result += 1
        break
    if (head_x, head_y) in snake:
        result += 1
        break

    # [3-1] 이동한 칸에 사과가 있으면, 그 칸에 있던 사과 x, 꼬리 안움직
    if (head_x, head_y) in apples:
        apples.remove((head_x, head_y))
        snake.appendleft((head_x, head_y))
    # [3-2] 이동한 칸에 사과 없으면, 몸 길이를 줄여 꼬리가 위치한 칸 비움
    else:
        snake.appendleft((head_x, head_y))
        snake.pop()
    result += 1

print(result)