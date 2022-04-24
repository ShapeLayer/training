# 문제 제시 값
origin = 10000000
rate = .03
saves = 3

# 문제 제시 알고리즘
res = origin * (1 + rate) ** saves

print(f'원금 : {origin}')
print(f'이자율 : {rate*100}%')
print(f'예치기간 : {saves}년')
print(f'미래가치: {round(res, 1)}')
