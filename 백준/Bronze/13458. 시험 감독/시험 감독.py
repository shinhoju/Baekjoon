test_places = int(input())
test_members = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for i in test_members:
    i -= B
    result += 1

    if i > 0:
        result += (i//C)

        if i % C > 0:
            result += 1

print(result)