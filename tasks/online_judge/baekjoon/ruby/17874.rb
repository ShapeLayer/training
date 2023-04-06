n, h, v = gets.split.map(&:to_i)
res = (h > (n - h) ? h : (n - h)) * (v > (n - v) ? v : (n - v))
puts res * 4
