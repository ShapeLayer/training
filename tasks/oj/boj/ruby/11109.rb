for _i in 1.. gets.to_i do
  d, n, s, p = gets.split(' ').map(&:to_i)
  if d + p * n < s * n then # 병렬
    puts "parallelize"
  elsif d + p * n > s * n then # 직렬
    puts "do not parallelize"
  else # 상관없음
    puts "does not matter"
  end
end