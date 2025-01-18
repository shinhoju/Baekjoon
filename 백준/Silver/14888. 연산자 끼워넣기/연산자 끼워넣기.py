# 연산자 끼워넣기
# 구현, 전체 탐색
# 최대값 / 최소값 한 줄에 하나씩 출력
from itertools import permutations


N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))
# 연산자: + - * //
#       0 1 2 3
# 개수   n n n n

# 구하고 싶은 것
results = []

# 연산 함수
def operation(seq, s, b):
    global keys, A
    # 앞에서 부터 순서대로
    # 음수의 나눗셈: -( -(음수) // (양수) )
    if seq == N-1:
        return s

    else:
    # 나눗셈
        if keys[seq] == 3:
            if s < 0:
                s = -((-s) // A[b])
            else:
                s = s // A[b]

        # 덧셈
        elif keys[seq] == 0:
            s = s + A[b]

        # 뺄셈
        elif keys[seq] == 1:
            s = s - A[b]

        # 곱셈
        elif keys[seq] == 2:
            s = s * A[b]

        return operation(seq+1, s, b+1)


ops_list = []
for i, o in enumerate(ops):
    if not len(ops_list):
        ops_list = [i] * o

    else:
        ops_list = ops_list + ([i] * o)


# [1] 연산자 순서 정하기 (dict 형 keys 중복될 수 없다는 것을 이용해 저장)
ops_dict = {}
for temp in permutations(ops_list, len(ops_list)):
    ops_dict[temp] = None

# [2] 모든 조합에 대해 전체 탐색
for keys in ops_dict.keys():
    results.append(operation(0, A[0], 1))

print(max(results))
print(min(results))