$MOD = 1e3.to_i
for _i in 1..gets.to_i
  n = gets.to_i
  res = 1
  for i in 1..n
    res *= i
    while res % 10 == 0
      res /= 10
    end
    res %= $MOD
  end
  puts res % 10
end
