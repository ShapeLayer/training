a, b = gets.split().map(&:to_i)
arr = [a+b, a-b]

puts arr.max
puts arr.min