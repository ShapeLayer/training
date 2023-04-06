counts = [0, 0]
for _i in 1..gets.to_i
  a, b = gets.split.map(&:to_i)
  if a > b then counts[0] += 1
  elsif a < b then counts[1] += 1
  end
end
puts counts.join(" ")
