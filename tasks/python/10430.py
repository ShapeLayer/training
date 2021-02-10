a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(str((a+b)%c))
print(str(((a%c)+(b%c))%c))
print(str((a*b)%c))
print(str(((a%c)*(b%c))%c))