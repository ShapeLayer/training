a, b = gets.split().map(&:to_i)
puts ((b-a).abs+1)*(a+b)/2