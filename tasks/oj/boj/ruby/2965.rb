a, b, c = gets.split.map(&:to_i)
puts [c - b, b - a].max - 1
