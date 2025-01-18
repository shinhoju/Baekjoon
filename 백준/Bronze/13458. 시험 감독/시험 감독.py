# 시험 감독
# 모든 응시자를 감시하기 위한 감독관의 총 수 구하기
# 단순 구현

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0

for a in A:
    # [1] 총감독관 1명
    result += 1
    a = a - B

    # 총감독관 배치 후에도 더 감독해야 할 응시자 있는 경우:
    if a > 0:
        quo = a // C
        re = a % C

        if re == 0:
            result += quo
        else:
            result += (quo+1)

print(result)