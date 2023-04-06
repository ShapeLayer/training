n, res = gets.to_i, 1
for i in 2..n
  res *= i
  res %= 10
end
puts res