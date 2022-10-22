$MOD = 1e12.to_i
$RES = 1e5.to_i
n = gets.to_i
res = 1
for i in 1..n
  res *= i
  while res % 10 == 0
    res /= 10
  end
  res %= $MOD
end
puts '%05d' % (res % $RES)
