from collections import deque

n, m, k = map(int, input().split(' '))

# 양분 양 배열
a = [list(map(int, input().split(' '))) for _ in range(n)]
# 초기 밭 배열
graph = [[5] * n for _ in range(n)]
# 나무들 상태 저장할 배열
trees = [[deque() for _ in range(n)] for _ in range(n)]
# 위치별 죽은 나무들 저장할 배열
dead_trees = [[list() for _ in range(n)] for _ in range(n)]

# 입력받은 초기 나무 위치, 나이 저장
for _ in range(m):
    x, y, z = map(int, input().split(' '))
    trees[x - 1][y - 1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 봄, 여름 처리할 함수
def spring_summer():
    for i in range(n):
        for j in range(n):
            len_ = len(trees[i][j]) # 현재 위치에 있는 나무 총 개수
            # 현재 위치의 나무들 탐색
            for k in range(len_):
                # 나무가 죽는 경우
                if graph[i][j] < trees[i][j][k]:
                    # 죽는 나무들은 따로 저장
                    for _ in range(k, len_):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                # 나무가 양분 먹고 성장하는 경우
                else:
                    graph[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
    # 죽은 나무들 만큼 양분 저장
    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                graph[i][j] += dead_trees[i][j].pop() // 2

# 가을, 겨울 처리할 함수
def fall_winter():
    for i in range(n):
        for j in range(n):
            # 현재 위치의 나무들 탐색
            for k in range(len(trees[i][j])):
                # 현재 나무의 나이가 씨를 뿌릴 수 있는 상태인 경우
                if trees[i][j][k] % 5 == 0:
                    # 8방향에 씨 뿌림
                    for t in range(8):
                        nx = i + dx[t]
                        ny = j + dy[t]
                        # 범위 체크
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        # 새로 태어난 나무들 앞으로 삽입
                        trees[nx][ny].appendleft(1)
            # 밭에 양분 추가
            graph[i][j] += a[i][j]


for i in range(k):
    spring_summer()
    fall_winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)