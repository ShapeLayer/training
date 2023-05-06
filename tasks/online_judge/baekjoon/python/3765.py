from sys import stdin

if __name__ == '__main__':
    try:
        while True:
            print(input())
    except EOFError:
        exit(0)
