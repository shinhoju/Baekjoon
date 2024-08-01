from itertools import combinations, permutations

N = int(input())
board = []
for _ in range(N):
  board.append(list(map(int, input().split())))


def factorial(x, e):
  result = 1
  while True:
    if x != (e - 1):
      result *= x
      x = x - 1
    else:
      return result

  
# 능력치 차이의 최소값 반환
half_point = (factorial(N, (N // 2 + 1)) // factorial(N // 2, 1)) // 2
units = set(range(1, N + 1))
diff = []

for i, c in enumerate(combinations(range(1, N+1), N // 2)):
  if i >= half_point:
    break
  team1 = set(c)
  team2 = units - team1

  h1 = 0
  h2 = 0

  for p1, p2 in permutations(team1, 2):
    h1 += board[p1-1][p2-1]

  for p1, p2 in permutations(team2, 2):
    h2 += board[p1-1][p2-1]

  diff.append(abs(h1 - h2))

print(min(diff))