N = int(input())

# 학생 번호 / 좋아 하는 친구 1,2,3,4
students = dict()
for _ in range(N**2):
    a, b, c, d, e = map(int, input().split())
    students[a] = [b, c, d, e]

board = [[0] * N for _ in range(N)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_friends(s, x, y):
    global visited, board
    max_v = 0
    for n in range(4):
        nx, ny = x + dx[n], y + dy[n]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        # 인접한 칸에 친한 친구가 있으면
        if board[nx][ny] in s:
            visited[x][y] += 1
            max_v = max(max_v, visited[x][y])

    return max_v


for student, friends in students.items():
    visited = [[0] * N for _ in range(N)]
    # [1] 비어 있는 칸 중 좋아 하는 학생이 인접한 칸에 가장 많은 칸
    # visited 각 칸에 좋아 하는 학생 수
    max_v = 0
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                v = find_friends(friends, i, j)
                max_v = max(max_v, v)
            else:
                # 다른 학생이 있는 칸일 경우, -1 표시
                visited[i][j] = -1

    max_list = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == max_v:
                max_list.append((i, j))

    if len(max_list) == 1:
        x, y = max_list[0]
        board[x][y] = student
    else:
        # [2] 1을 만족 하는 칸이 여러 개일 경우, 인접 칸 중 빈 칸이 가장 많은 칸
        x, y = 0, 0
        max_cnt = 0
        for i, j in max_list[::-1]:
            cnt = 0
            for n in range(4):
                ni, nj = i + dx[n], j + dy[n]
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                if not board[ni][nj]:
                    cnt += 1
            if max_cnt <= cnt:
                max_cnt = cnt
                x, y = i, j
        board[x][y] = student

# 만족도 구하기
sum_v = 0
for i in range(N):
    for j in range(N):
        v = 0
        s = board[i][j]
        for n in range(4):
            ni, nj = i + dx[n], j + dy[n]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if board[ni][nj] in students[s]:
                v += 1
        if v == 0:
            sum_v += 0
        else:
            sum_v += (10 ** (v-1))

print(sum_v)