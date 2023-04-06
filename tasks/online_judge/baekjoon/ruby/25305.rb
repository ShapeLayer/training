n, k = gets.split.map(&:to_i)
x = gets.split.map(&:to_i).sort.reverse
puts x[k-1]
