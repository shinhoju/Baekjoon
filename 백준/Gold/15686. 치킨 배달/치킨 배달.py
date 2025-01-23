# 치킨 배달
# 2 <= N <= 50, 1 <= M <= 13


from itertools import combinations

N, M = map(int, input().split())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))


def manhattan_len(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# [1] 집 치킨집 위치 구하기
homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

# [2] M 보다 현재 치킨 집이 작거나 같은 경우: 바로 최소 치킨 거리 구함
if len(chickens) <= M:
    sum_dis = 0
    for h_x, h_y in homes:
        temp = 200
        for c_x, c_y in chickens:
            dis = manhattan_len(h_x, h_y, c_x, c_y)
            if dis < temp:
                temp = dis
        sum_dis += temp

# [3] M 보다 현재 치킨 집이 많은 경우: combination 활용
else:
    sum_dis = 2**16
    for selected_chicken in combinations(chickens, M):
        sum_temp = 0
        for h_x, h_y in homes:
            temp = 200
            for c_x, c_y in selected_chicken:
                dis = manhattan_len(h_x, h_y, c_x, c_y)
                if dis < temp:
                    temp = dis
            sum_temp += temp
        if sum_temp < sum_dis:
            sum_dis = sum_temp

print(sum_dis)