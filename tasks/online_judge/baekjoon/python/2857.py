if __name__ == '__main__':
    agents = []
    for i in range(1, 6):
        if 'FBI' in input():
            agents.append(i)
    if len(agents) == 0:
        print('HE GOT AWAY!')
    else:
        print(*agents)
