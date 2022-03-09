var = gets.split(" ").map(&:to_i)
a = [(var[0]-1) % 4, (var[0].to_f/4.0).ceil]
b = [(var[1]-1) % 4, (var[1].to_f/4.0).ceil]
puts (a[0]-b[0]).abs + (a[1]-b[1]).abs