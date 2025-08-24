# 3190. 뱀

from collections import deque

N = int(input())
K = int(input())

apples = []
for _ in range(K):
    apples.append(tuple(map(int, input().split())))

L = int(input())
move = {}                       # -1: 왼쪽 / 1: 오른쪽 회전
for _ in range(L):
    x, c = input().split()
    move[int(x)] = -1 if c == "L" else 1

snake = deque()
snake.append((1, 1))
snake_d = 0

# 오른쪽 -> 시계 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def in_range(x, y):
    if x < 1 or x > N or y < 1 or y > N:
        return False
    else:
        return True


result = 0
while True:
    result += 1

    # [1] 머리를 다음 칸에 위치
    hx, hy = snake[0][0], snake[0][1]
    n_hx, n_hy = hx + dx[snake_d], hy + dy[snake_d]

    # 종료 조건: 벽이나 자기 자신의 몸과 부딛힘
    if not in_range(n_hx, n_hy):
        break
    if (n_hx, n_hy) in snake:
        break

    # [2] 사과 o: 사과 먹고 꼬리 움직 x
    if (n_hx, n_hy) in apples:
        snake.appendleft((n_hx, n_hy))
        apples.remove((n_hx, n_hy))
    # [3] 사과 x: 꼬리 - 1칸
    else:
        snake.pop()
        snake.appendleft((n_hx, n_hy))

    # [4] 방향 전환
    if result in move.keys():
        snake_d = (snake_d + move[result]) % 4

print(result)