arr = gets.split().map(&:to_i)
a, b = arr[0] + arr[3], arr[1] + arr[2]
puts (a - b).abs