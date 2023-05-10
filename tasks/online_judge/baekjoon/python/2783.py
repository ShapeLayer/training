if __name__ == '__main__':
    costs = []
    x, y = map(int, input().split())
    costs.append(x / y)
    for t in range(int(input())):
        x, y = map(int, input().split())
        costs.append(x / y)
    costs.sort()
    print(costs[0] * 1000)
