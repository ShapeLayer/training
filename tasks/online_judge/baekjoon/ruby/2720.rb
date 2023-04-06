for _i in 1..gets.to_i
  c = gets.to_i
  res = []
  [25, 10, 5, 1].each do |div|
    res += [c / div]
    c %= div
  end
  puts res.join(' ')
end
