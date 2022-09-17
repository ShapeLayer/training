c, k, p = map(int, input().split())
print( (k * (c+1) * c) // 2 + (p * c * (c+1) * (2*c+1)) // 6 )
