d, h, w = gets.split().map(&:to_i)
d_ratio = d / ((h**2 + w**2) ** 0.5)
puts "%d %d" % [d_ratio * h, d_ratio * w]