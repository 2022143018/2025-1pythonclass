# 2025.04.02 파일썬 수업 프로젝트 두 번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지의 숫자 중, 가장 많은 단계를 거쳐서 1호 가는 수는 무엇인가?, 가장 많은 단계는 몇 단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3 * n + 1
#  예: 5 -> 16 -> 8 -> 4 -> 2 -> 1  (5단계)
import numpy as np
import statistics
import time

from p02Collatzfunc import  collatz

MAXNUM = 100

# 2025.04.09. 우박수 프로젝트 두 번째 : 기본 통계량 구하기
# numpy 배열, list 두가지 방식으로 시험
# 구하는 통계량 : 최대값, 평균, 중앙값, 표준편차, 최빈값




# list 방식

start = time.time()

ncountl = []

for n in range(1,MAXNUM):
    # print(f'{n=}')
    ncount = collatz(n)
    ncountl.append(ncount)


# print(ncountl)
# print(sum(ncountl) / len(ncountl))


# 최대값, 평균, 중앙값, 표준편차, 최빈값

print(f'최대값 = {max(ncountl)}')
print(f'평균 ={statistics.mean(ncountl): 5f}')
print(f'중앙값 ={statistics.median(ncountl)}')
print(f'표준편차 ={statistics.stdev(ncountl): 5f}')
# print(f'최빈값 ={statistics.mode(ncountl)}')

end = time.time()
print(f'{end - start: .5f}초가 걸렸습니다')

# numpy 방식

start = time.time()

ncounta = np.zeros(MAXNUM-1)

for n in range(1,MAXNUM):
    # print(f'{n=}')
    ncount = collatz(n)
    ncounta[n-1] = ncount


# 최대값, 평균, 중앙값, 표준편차, 최빈값

print(f'최대값 = {np.max(ncounta)}')
print(f'평균 ={np.mean(ncounta): 5f}')
print(f'중앙값 = {np.median(ncounta)}')
print(f'표준편차 ={np.std(ncounta): 5f}')
# print(f'최빈값 = {np.bincount(ncounta).argmax()}')

end = time.time()
print(f'{end - start: .5f}초가 걸렸습니다')