n = int(input())
if not n: exit()
print('int a;')
prev = 'a'
for i in range(1, n+1):
    ptr = '*' * i
    num = str(i) if i != 1 else ''
    print(f'int {ptr}ptr{num} = &{prev};')
    prev = f'ptr{num}'