# 스타트와 링크
from itertools import combinations

N = int(input())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

# [1] 팀 나누기
teams = set()
temp = set(range(N))
for comb in combinations(range(N), N//2):
    team = sorted([comb, tuple(temp-set(comb))])
    teams.add(tuple(team))

# [2] 능력치 table 조회하여 차 구하기
result = 2**16
for start, link in teams:
    # start 팀의 능력치 합
    start_sum = 0
    for i in range(N//2):
        for j in range(i, N//2):
            s_i, s_j = start[i], start[j]
            start_sum = start_sum + table[s_i][s_j] + table[s_j][s_i]

    # link 팀의 능력치 합:
    link_sum = 0
    for i in range(N//2):
        for j in range(i, N//2):
            s_i, s_j = link[i], link[j]
            link_sum = link_sum + table[s_i][s_j] + table[s_j][s_i]

    temp_diff = abs(start_sum - link_sum)
    if temp_diff < result:
        result = temp_diff

print(result)