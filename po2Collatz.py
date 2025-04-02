# 2025.4.2 파이썬 수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자중, 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가?,가장 많은 단계는 몇단계인가
# 규칙: n이 짝수 -> n/2
#     n이 홀수 -> 3 * n + 1
# 예: 5 -> 16 ->8 -> 4 -> 2 -> 1 (5단계)

n = 5
if n % 2 == 1:
    print('n은 홀수')
else:
    print('n은 짝수')


n = 99
while n!= 1:
    if n %2 == 1:
        n = 3 * n + 1
    else:
        n = n / 2
    print(n)








n = 5
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence

# n = 5로 실행
n = 5
result = collatz_sequence(n)
print(" -> ".join(map(str, result)))




















