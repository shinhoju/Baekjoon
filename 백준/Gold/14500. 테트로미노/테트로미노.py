# 14500. 테트로미노

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


# 대충 500만번 연산 드감
def tetris(x, y, n):
    if n == 0:
        return [(x, y), (x, y+1), (x, y+2), (x, y+3)]
    elif n == 1:
        return [(x, y), (x+1, y), (x+2, y), (x+3, y)]
    elif n == 2:
        return [(x, y), (x+1, y), (x+1, y+1), (x, y+1)]
    elif n == 3:
        return [(x, y), (x+1, y), (x+2, y), (x+2, y+1)]
    elif n == 4:
        return [(x, y+1), (x+1, y+1), (x+2, y+1), (x+2, y)]
    elif n == 5:
        return [(x, y), (x, y+1), (x, y+2), (x+1, y)]
    elif n == 6:
        return [(x, y), (x, y+1), (x+1, y+1), (x+2, y+1)]
    elif n == 7:
        return [(x+1, y), (x+1, y+1), (x+1, y+2), (x, y+2)]
    elif n == 8:
        return [(x, y), (x, y+1), (x, y+2), (x+1, y+2)]
    elif n == 9:
        return [(x, y), (x, y+1), (x+1, y), (x+2, y)]
    elif n == 10:
        return [(x, y), (x+1, y), (x+1, y+1), (x+1, y+2)]
    elif n == 11:
        return [(x, y), (x+1, y), (x+1, y+1), (x+2, y+1)]
    elif n == 12:
        return [(x+1, y), (x+2, y), (x, y+1), (x+1, y+1)]
    elif n == 13:
        return [(x+1, y), (x, y+1), (x+1, y+1), (x, y+2)]
    elif n == 14:
        return [(x, y), (x, y+1), (x+1, y+1), (x+1, y+2)]
    elif n == 15:
        return [(x, y), (x, y+1), (x, y+2), (x+1, y+1)]
    elif n == 16:
        return [(x+1, y), (x+1, y+1), (x+1, y+2), (x, y+1)]
    elif n == 17:
        return [(x+1, y), (x, y+1), (x+1, y+1), (x+2, y+1)]
    elif n == 18:
        return [(x, y), (x+1, y), (x+2, y), (x+1, y+1)]


def in_range(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    else:
        return True


result = 0
for r in range(N):
    for c in range(M):
        for i in range(19):
            c1, c2, c3, c4 = tetris(r, c, i)
            temp = 0
            for xx, yy in (c1, c2, c3, c4):
                if not in_range(xx, yy):
                    continue
                temp += arr[xx][yy]
            if temp > result:
                result = temp

print(result)