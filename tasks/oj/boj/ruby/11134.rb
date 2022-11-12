t = gets.to_i
for _i in 1..t
  n, c = gets.split.map(&:to_i)
  puts n % c == 0 ? n / c : n / c + 1
end
