N, M = map(int, input().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

tetris = {0: lambda x,y: [(x, y), (x, y+1), (x, y+2), (x, y+3)],
          1: lambda x,y: [(x, y), (x, y+1), (x+1, y), (x+1, y+1)],
          2: lambda x,y: [(x, y), (x+1, y), (x+2, y), (x+2, y+1)],
          3: lambda x,y: [(x, y), (x+1, y), (x+1, y+1), (x+2, y+1)],
          4: lambda x,y: [(x, y), (x, y+1), (x, y+2), (x+1, y+1)],
          5: lambda x,y: [(x, y), (x+1, y), (x+2, y), (x+3, y)],
          6: lambda x,y: [(x, y), (x+1, y), (x, y+1), (x, y+2)],
          7: lambda x,y: [(x, y), (x, y+1), (x+1, y+1), (x+2, y+1)],
          8: lambda x,y: [(x, y), (x, y+1), (x, y+2), (x-1, y+2)],
          9: lambda x,y: [(x, y), (x, y+1), (x-1, y+1), (x-2, y+1)],
          10: lambda x,y: [(x, y), (x+1, y), (x+1, y+1), (x+1, y+2)],
          11: lambda x,y: [(x, y), (x, y+1), (x+1, y), (x+2, y)],
          12: lambda x,y: [(x, y), (x, y+1), (x, y+2), (x+1, y+2)],
          13: lambda x,y: [(x, y), (x, y+1), (x-1, y+1), (x-1, y+2)],
          14: lambda x,y: [(x, y), (x+1, y), (x, y+1), (x-1, y+1)],
          15: lambda x,y: [(x, y), (x, y+1), (x+1, y+1), (x+1, y+2)],
          16: lambda x,y: [(x, y), (x, y+1), (x-1, y+1), (x+1, y+1)],
          17: lambda x,y: [(x, y), (x-1, y+1), (x, y+1), (x, y+2)],
          18: lambda x,y: [(x, y), (x+1, y), (x+2, y), (x+1, y+1)],
}

result = 0

for i in range(N):
    for j in range(M):
        for n in range(19):
            tet = tetris[n](i, j)
            # 경계 값
            x_s = [x[0] for x in tet]
            y_s = [x[1] for x in tet]
            # 경계 확인
            if min(x_s) < 0 or min(y_s) < 0 or max(x_s) >= N or max(y_s) >= M:
                continue
            temp = 0
            for m in range(4):
                tx, ty = tet[m]
                temp += paper[tx][ty]
            result = max(result, temp)

print(result)