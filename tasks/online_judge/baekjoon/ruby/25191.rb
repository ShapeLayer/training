a = gets.to_i
b, c = gets.split.map(&:to_i)
puts [a, b / 2 + c].min
