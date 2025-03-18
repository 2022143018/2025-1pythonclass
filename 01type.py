# 2025.3.12
# 파이썬 수업 - 변수, 타입, 출력
# 타입 (형) - 정수 : int (integer)
#            실수 : float (floating point)
#             문자열: str(string)
#             논리값: bool (boolean)

title = "시간계산"
sec = 3700
min = sec / 60
bigger = min > sec
print(sec, min, bigger)
print(type(title)), type(sec), type(min), type(bigger)

a = int(10.999989)  # floor 버림, ceiling 올림, round 반올림
b = float(10.3)
c = str(10.3)
print(type(a), type(b), type(c))
print(a)

sec1 = 1300; sec2 = 500
seca = sec1 + sec2
secs = sec1 - sec2
secm = sec1 * sec2

secd = sec1 / sec2


secq = sec1 // sec2
seqr = sec1 % sec2
print(f'{seca=}, {secs=},{secm=}, {secd=}, {secq=}, {seqr=}')  #f string

# 화씨를 섭씨로 바꿈
# Tc = (Tf - 21) * 5/9
# Tf = (Tc * 9/5) + 32
tf = 39
tc = (tf - 32) * 5/9
print(f'{tf=} ===> {tc=}')

tc = 37.7
tf = tc * 9 / 5 + 32
print(f'{tc=} ===> {tf=}')

print(2 ** 3, 2 ** (1/2), 2 ** (-1/2))
# 사칙연산중에서 0으로 나누는 것은 허용하지 않음
print(3/0)
