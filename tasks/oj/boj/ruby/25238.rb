a, b = gets.split().map(&:to_i)
puts a * (100 - b) / 100 >= 100 ? 0 : 1