gets = int(input())
puts = 0
while gets:
    puts += (gets % 10) ** 5
    gets //= 10
print(puts)
