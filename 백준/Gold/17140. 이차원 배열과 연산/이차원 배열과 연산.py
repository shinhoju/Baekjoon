R, C, K = map(int, input().split())
R -= 1
C -= 1
a = []
for _ in range(3):
    a.append(list(map(int, input().split())))


def freq(x):
    return x[1]


def r_op():
    temp = []
    max_len = 0
    for row in a:
        rows = []
        count = [0] * 1000
        for r in row:
            count[r] += 1
        for i, c in enumerate(count):
            if c != 0 and i != 0:
                rows.append((i, c))
        rows.sort()
        rows.sort(key=freq)
        temp.append(rows)
        max_len = max(max_len, len(rows))
    result = [[0] * (max_len * 2) for _ in range(len(a))]
    for i, ts in enumerate(temp):
        num = 0
        for t in ts:
            for ii, tt in enumerate(t):
                result[i][ii+num] = tt
                if ii == 1:
                    num += 2

    if len(result) >= 100 or len(result[0]) >= 100:
        ttemp = [[0] * 100 for _ in range(100)]
        for i in range(100):
            for j in range(100):
                ttemp[i][j] = result[i][j]
        return ttemp

    return result


def rotate():
    global a
    temp = [[0] * len(a) for _ in range(len(a[0]))]
    for r in range(len(a)):
        for c in range(len(a[0])):
            temp[c][r] = a[r][c]
    a = temp


cnt = 0             # 몇 초 걸리는 지 세기
while True:
    # 종료 조건
    if R < len(a) and C < len(a[0]):
        if a[R][C] == K:
            break
        if cnt == 100 and a[R][C] != K:
            cnt = -1
            break
    elif cnt == 100:
        cnt = -1
        break

    # R, C 연산 조건
    if len(a) >= len(a[0]):
        a = r_op()
        cnt += 1
    else:
        rotate()
        a = r_op()
        rotate()
        cnt += 1



print(cnt)