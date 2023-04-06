d, h, m = gets.split().map(&:to_i)
base = 11 + 11 * 60 + 11 * 60 * 24;
res = m + h * 60 + d * 60 * 24 - base;
puts res >= 0 ? res : -1