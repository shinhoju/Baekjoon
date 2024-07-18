N = int(input())
schedule = []
for _ in range(N):
    schedule.append(list(map(int, input().split())))

pay = [0] * (N+1)

for i in range(N):
    for j in range(i+schedule[i][0], N+1):
        if pay[j] < pay[i] + schedule[i][1]:
            pay[j] = pay[i] + schedule[i][1]

print(pay[-1])