from sys import stdin
gets = stdin.readline
n, m = map(int, gets().split())
pokemon_by_num = []
pokemon_by_key = {}
for i in range(1, n+1):
    puts = gets().rstrip()
    pokemon_by_num.append(puts)
    pokemon_by_key[puts] = i
for _ in range(m):
    puts = gets().rstrip()
    try:
        print(pokemon_by_num[int(puts)-1])
    except ValueError:
        print(pokemon_by_key[puts])