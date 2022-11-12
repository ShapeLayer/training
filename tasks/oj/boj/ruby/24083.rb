a, b = gets.to_i, gets.to_i
res = (a + b) % 12
puts res != 0 ? res : 12
