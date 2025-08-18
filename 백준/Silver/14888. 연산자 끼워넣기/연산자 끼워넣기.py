# 14888. 연산자 끼워넣기
from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
# ops = [+, -, *, //]
ops_num = list(map(int, input().split()))


mn = 1e10
mx = -1e10

ops = []
for i in range(len(ops_num)):
    if ops_num[i]:
        for _ in range(ops_num[i]):
            ops.append(i)


def calculate(x, y, o):
    if o == 0:
        return x + y
    elif o == 1:
        return x - y
    elif o == 2:
        return x * y
    else:
        if x < 0:
            return -((-x) // y)
        else:
            return x // y


for op in permutations(ops, len(ops)):
    # 순서대로 계산

    xi = nums[0]
    for yi, oi in zip(range(1, len(nums)), op):
        xi = calculate(xi, nums[yi], oi)

    # 최대 / 최소 갱신
    if mx < xi:
        mx = xi
    if mn > xi:
        mn = xi

print(mx)
print(mn)