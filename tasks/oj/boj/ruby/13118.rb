arr = gets.split.map(&:to_i)
x, y, r = gets.split.map(&:to_i)
puts arr.index(x) != nil ? arr.index(x) + 1 : 0
