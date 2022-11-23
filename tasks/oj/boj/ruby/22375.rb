x, y = gets.split.map(&:to_i)
r = gets.to_i

puts "%d %d" % [x - r, y + r]
puts "%d %d" % [x + r, y + r]
puts "%d %d" % [x + r, y - r]
puts "%d %d" % [x - r, y - r]
