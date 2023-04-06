vk, jk = gets.split().map(&:to_i)
va, ja = gets.split().map(&:to_i)
vh, dh, jh = gets.split().map(&:to_i)
puts vh * dh * jh * (vk * jk + va * ja)