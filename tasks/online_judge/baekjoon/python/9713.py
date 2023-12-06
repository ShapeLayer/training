if __name__ == '__main__':
    for _i in range(int(input())):
        gets = int(input())
        print(sum([j if j % 2 != 0 else 0 for j in range(1, gets + 1)]))
