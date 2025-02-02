# 테트로미노
# 브루트포스

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))


def t1(x, y):
    sums = 0
    if x + 3 < N:
        t11 = maps[x][y] + maps[x+1][y] + maps[x+2][y] + maps[x+3][y]
        sums = max(sums, t11)

    if y + 3 < M:
        t12 = maps[x][y] + maps[x][y+1] + maps[x][y+2] + maps[x][y+3]
        sums = max(sums, t12)

    return sums

def t2(x, y):
    if x + 1 < N and y + 1 < M:
        t21 = maps[x][y] + maps[x+1][y] + maps[x][y+1] + maps[x+1][y+1]
        return t21
    else:
        return 0

def t3(x, y):
    sums = 0
    if x + 2 < N and y + 1 < M:
        t31 = maps[x][y] + maps[x+1][y] + maps[x+2][y] + maps[x+2][y+1]
        t32 = maps[x+2][y] + maps[x][y+1] + maps[x+1][y+1] + maps[x+2][y+1]
        t33 = maps[x][y] + maps[x][y+1] + maps[x+1][y+1] + maps[x+2][y+1]
        t34 = maps[x][y] + maps[x][y+1] + maps[x+1][y] + maps[x+2][y]
        sums = max(sums, t31, t32, t33, t34)

    if x + 1 < N and y + 2 < M:
        t35 = maps[x][y] + maps[x][y+1] + maps[x][y+2] + maps[x+1][y]
        t36 = maps[x][y] + maps[x+1][y] + maps[x+1][y+1] + maps[x+1][y+2]
        t37 = maps[x+1][y] + maps[x+1][y+1] + maps[x+1][y+2] + maps[x][y+2]
        t38 = maps[x][y] + maps[x][y+1] + maps[x][y+2] + maps[x+1][y+2]
        sums = max(sums, t35, t36, t37, t38)

    return sums

def t4(x, y):
    sums = 0
    if x + 2 < N and y + 1 < M:
        t41 = maps[x][y] + maps[x+1][y] + maps[x+1][y+1] + maps[x+2][y+1]
        t42 = maps[x][y+1] + maps[x+1][y] + maps[x+1][y+1] + maps[x+2][y]
        sums = max(sums, t41, t42)

    if x + 1 < N and y + 2 < M:
        t43 = maps[x][y+1] + maps[x][y+2] + maps[x+1][y] + maps[x+1][y+1]
        t44 = maps[x][y] + maps[x][y+1] + maps[x+1][y+1] + maps[x+1][y+2]
        sums = max(sums, t43, t44)

    return sums

def t5(x, y):
    sums = 0
    if x + 2 < N and y + 1 < M:
        t51 = maps[x+1][y] + maps[x][y+1] + maps[x+1][y+1] + maps[x+2][y+1]
        t52 = maps[x][y] + maps[x+1][y] + maps[x+2][y] + maps[x+1][y+1]
        sums = max(sums, t51, t52)

    if x + 1 < N and y + 2 < M:
        t53 = maps[x][y] + maps[x][y+1] + maps[x][y+2] + maps[x+1][y+1]
        t54 = maps[x][y+1] + maps[x+1][y] + maps[x+1][y+1] + maps[x+1][y+2]
        sums = max(sums, t53, t54)

    return sums


result = 0

for i in range(N):
    for j in range(M):
        t1_max = t1(i, j)
        t2_max = t2(i, j)
        t3_max = t3(i, j)
        t4_max = t4(i, j)
        t5_max = t5(i, j)
        result = max(t1_max, t2_max, t3_max, t4_max, t5_max, result)

print(result)