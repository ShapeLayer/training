a, b, c = gets.split().map(&:to_i)
puts a * [b, c].max / [b, c].min
