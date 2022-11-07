n = gets.to_i
scores = gets.split.map(&:to_i)
puts scores.max - scores.min
