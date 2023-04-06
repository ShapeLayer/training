puts = []
for _i in range(int(input())):
    puts += [int(input())]
puts.sort(reverse=True)
print(sum(puts) - sum(puts[2::3]))