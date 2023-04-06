n = gets.to_i

for i in 0..n-1 do
  puts gets.split.map(&:to_i).sort.reverse[2]
end