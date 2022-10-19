res = [0, 0]
offset = [6, 3, 2, 1, 2]
for i in 0..1
  get = gets.split().map(&:to_i)
  for j in 0..4
    res[i] += get[j] * offset[j]
  end
end
puts '%d %d' % [res[0], res[1]]