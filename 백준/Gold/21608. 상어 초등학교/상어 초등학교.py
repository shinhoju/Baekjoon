# 상어 초등학교

N = int(input())
students = []
for _ in range(N**2):
    students.append(list(map(int, input().split())))

# 인접한 칸, 오 왼 상 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

classroom = [[0] * N for _ in range(N)]

student_dict = {}


for student in students:
    # [1] 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸 선택
    s = student[0]
    friends = student[1:]
    student_dict[s] = friends

    candidate_seat1 = []
    num_like = -1
    for i in range(N):
        for j in range(N):
            # 누가 앉아 있으면 자리 선택 못함
            if classroom[i][j] != 0:
                continue

            like = 0
            for n in range(4):
                ni, nj = i + dx[n], j + dy[n]
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                if classroom[ni][nj] in friends:
                    like += 1

            if num_like < like:
                num_like = like
                candidate_seat1 = [(i, j)]
            elif num_like == like:
                candidate_seat1.append((i, j))


    # 후보 자리가 1개이면 그 자리에 앉힘
    if len(candidate_seat1) == 1:
        classroom[candidate_seat1[0][0]][candidate_seat1[0][1]] = s

    # [2] 1 만족 자리가 여러 개인 경우: 가장 빈 칸이 많은 자리 선택
    else:
        candidate_seat2 = []
        num_vacancy = -1
        for cx, cy in candidate_seat1:
            vacancy = 0
            for n in range(4):
                ni, nj = cx + dx[n], cy + dy[n]
                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                if classroom[ni][nj] == 0:
                    vacancy += 1

            if num_vacancy < vacancy:
                num_vacancy = vacancy
                candidate_seat2 = [(cx, cy)]
            elif num_vacancy == vacancy:
                candidate_seat2.append((cx, cy))

        # [3] 2 만족 칸 여러 개일 경우: 행/열 번호 가장 작은 자리
        classroom[candidate_seat2[0][0]][candidate_seat2[0][1]] = s

# 만족도 구하기
result = 0
for i in range(N):
    for j in range(N):
        temp = 0
        for n in range(4):
            ni, nj = i + dx[n], j + dy[n]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if classroom[ni][nj] in student_dict[classroom[i][j]]:
                temp += 1
        if temp > 0:
            result += (10 ** (temp - 1))

print(result)