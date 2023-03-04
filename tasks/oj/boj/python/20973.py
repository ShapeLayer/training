# 이 문제를 더 간단하게 풀 수 있는 방법이 있을것 같으나
# cowphabet을 차례로 출력하는 문제로 받아들여서 코드가 복잡함
order = list(input())
says = input()
cowphabet = list(order)
i = 0
cnt = 0
flag = True
for say in says:
    if not flag:
        flag = True
    while flag:
        if i >= len(order):
            cnt += 1
            cowphabet = list(order)
            i = 0
        while i < len(order):
            if cowphabet[i] == say:
                cowphabet[i] = cowphabet[i].upper()
                flag = False
                break
            i += 1

print(cnt+1)