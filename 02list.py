# 2025.3.18
# 파이썬 리스트 : 한개의 변수에 여러 값을 할달
colors = ['red', 'blue', 'green']
print(colors)   # 리스트 전체 풀력
print(colors[1])    # 리스트 두번째 원소 출력
print(colors[-1])   # 리스트 마지막 원소 출력
print(len(colors))  # 리스트 길이 출력
# 슬라이싱
cities = ['서울', '부산', '인천', '대전', '강릉', '논산', '포항']
print(cities[0:7]) #  cities[0:n] 0~ n-1 까지 표시
print(cities[:7])  #  0~6번째 원소
print(cities[:-1]) #  0~ -2 까지
print(cities[3:])  #  3 부터 끝 까지
print(cities[:])  #  전부 표시
print(cities[-4:]) # 뒤에서 부터 4번쨰 부터 표시
print(cities[:7:2]) # 처음 부터 6번째 원소 까지, 한칸씩 건너뜀
print(cities[::3]) # 처음 부터 끝 까지, 3칸씪 건너 뜀
print(cities[::-1]) # 처음 부터 끝 까지, 거꾸로
print(cities[4::-2])

# 리스트 의 추가
colors = ['red', 'blue', 'green']
colors.append('white')
print(colors[:])
colors.extend(['black', 'purple'])
print(colors[:])
colors.insert(1, 'orange')
print(colors[:])
colors.remove('purple')
print(colors[:])
colors[1] = 'sky'
print(colors[:])

#패킹, 언패킹
c1, _,  c2, c3, _, _  = colors
print(c1, c2, c3)

colors = ['red', 'blue', 'green']
cities = ['서울', '부산', '인천', '대전', '강릉', '논산', '포항']
combi = [colors, cities]
print(combi)
print(combi[1][2]) # 인천
#print(combi[2][3]) # 에러발생
bigcombi = [combi, [0,2,7]]
print(bigcombi)
print(len(bigcombi))
print(bigcombi[0][1][2]) #인천
print(f'{bigcombi[1][1]}') #2

# 퀴즈
first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]

order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]] # john = [soup, [lamb, chicken], apple]
del john[2]    # john = [soup, [lamb, chicken]]
john.extend([order[2][0:1]])    # john = [soup, [lamb, chicken], [apple]]
print(john)