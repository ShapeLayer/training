def solution(price, money):
    total = sum(price)
    answer = money-total
    if answer < 0:
        return -1
    return answer