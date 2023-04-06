whitespace = Array.new(101) { Array.new(101, false) }
for _i in 1..gets.to_i
  l, b = gets.split.map(&:to_i)
  for i in 1..10
    for j in 1..10
      whitespace[i+l][b+j] = true
    end
  end
end
size = 0
for i in 1..100
  for j in 1..100
    if whitespace[i][j] then size += 1 end
  end
end
puts size
