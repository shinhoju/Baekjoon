"""
톱니 바퀴 구성:
0 : N 극
1 : S 극

회전 방향:
1: 시계
-1: 반시계
"""

gear = []
for _ in range(4):
    gear.append(list(map(int, input())))

R = int(input())
rotate = []         # 회전 기어 번호, 방향
for _ in range(R):
    rotate.append(list(map(int, input().split())))

def rotate_gear(num, d):
    global temp_gear, gear
    temp = [0] * 8
    if d == 1:          # 시계 방향
        for i, g in enumerate(gear[num]):
            temp[(i + 1) % 8] = g
        temp_gear[num] = temp
    else:
        for i, g in enumerate(gear[num]):
            temp[(i - 1) % 8] = g
        temp_gear[num] = temp

def dfs(num, d):
    global gear

    visited[num] = True
    rotate_gear(num, d)

    for n_num in (num-1, num+1):
        if n_num < 0 or n_num >= 4 or visited[n_num]:
            continue
        if n_num == (num - 1):
            if gear[n_num][2] != gear[num][6]:
                dfs(n_num, -d)
        else:
            if gear[n_num][6] != gear[num][2]:
                dfs(n_num, -d)


for num, d in rotate:
    visited = [False] * 4
    temp_gear = [g[:] for g in gear]
    dfs(num-1, d)
    gear = temp_gear


score = 0
for i in range(4):
    if gear[i][0] == 1:
        score += 2**i

print(score)