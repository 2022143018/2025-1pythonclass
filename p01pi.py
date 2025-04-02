# 오일러 공식을 이용한 파이 근사값 구하기

# 기본계싼
p = 1
n = 1
p = p * ((2 * n + 1)**2 - 1)/ (2 * n + 1)**2
n = 2
p = p * ((2 * n + 1)**2 - 1)/ (2 * n + 1)**2
print(p*4)

# 루프로 변환 25.04.01
p=1
pilist = []
for n in range(1,200):
    p = p * ((2 * n + 1) ** 2 - 1) / (2 * n + 1) ** 2
    # print(p*4, ',')
    pilist.append(p*4)

##
import matplotlib.pyplot as plt
plt.plot(pilist)
plt.show()