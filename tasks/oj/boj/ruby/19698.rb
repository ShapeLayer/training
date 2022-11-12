n, w, h, l = gets.split.map(&:to_i)
res = (w / l) * (h / l)
puts n < res ? n : res
