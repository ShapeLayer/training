$dp = Array.new(2001){Array.new(2001, -1)}

def proc(n, k, m)
  a, b = 1, 1
  for i in (n-k+1..n).reverse_each
    a = a * i % m
  end
  for i in (2..k).reverse_each
    b = b * i % m
  end
  n, k = 1, m-2
  while k != 0
    if k & 1 != 0 then n = n * b % m end
    k >>= 1
    b = b * b % m
  end
  return a * n % m
end

n, k, m = gets.split().map(&:to_i)
res = 1
while n != 0 || k != 0
  res = res * proc(n % m, k % m, m) % m
  n /= m
  k /= m
end

puts res