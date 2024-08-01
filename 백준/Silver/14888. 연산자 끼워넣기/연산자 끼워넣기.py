from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

o1, o2, o3, o4 = map(int, input().split())
op = [1] * o1 + [2] * o2 + [3] * o3 + [4] * o4          # 덧셈 / 뺄셈 / 곱셈 / 나눗셈


# 재귀 형식 구현
def func(value, p_idx, n_idx, depth):              # (값), (연산자), (연산자 뒤의 숫자)
    global p, arr, temp

    # 종료 조건 : idx 끝에 도달
    if depth == (N - 1):
        temp = value
        return

    elif p[p_idx] == 1:
        result = value + arr[n_idx]
        func(result, p_idx + 1, n_idx + 1, depth + 1)

    elif p[p_idx] == 2:
        result = value - arr[n_idx]
        func(result, p_idx + 1, n_idx + 1, depth + 1)

    elif p[p_idx] == 3:
        result = value * arr[n_idx]
        func(result, p_idx + 1, n_idx + 1, depth + 1)

    elif p[p_idx] == 4:
        if abs(value) != value:     # 음수인 경우
            result = -(abs(value) // arr[n_idx])
        else:
            result = value // arr[n_idx]
        func(result, p_idx + 1, n_idx + 1, depth + 1)


values = []
for p in permutations(op):
    temp = 0
    func(arr[0], 0, 1, 0)
    values.append(temp)

print(max(values))
print(min(values))