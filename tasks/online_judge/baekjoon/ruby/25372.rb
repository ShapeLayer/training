for _i in 1..gets.strip.to_i
  pw = gets.strip
  puts 6 <= pw.length && pw.length <= 9 ? 'yes' : 'no'
end