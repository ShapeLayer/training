s = gets.to_i
n = 1
while (1 + n) * n / 2 <= s do
  n += 1
end
puts n-1