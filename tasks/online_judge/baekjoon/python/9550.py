from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    for i in range(int(input())): 
        n, k = map(int, input().split()) 
        candies = list(map(int, input().split()))
        result = 0
        for candy in candies:
            result += candy // k 
        print(result)
