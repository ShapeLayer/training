h, w, n, m = gets.split.map(&:to_f)
puts (h / (n + 1)).ceil * (w / (m + 1)).ceil
