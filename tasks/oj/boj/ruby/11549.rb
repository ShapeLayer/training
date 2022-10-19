tea = gets.to_i
ans = gets.split().map(&:to_i)
cnt = 0
for each in ans
  if each == tea then
    cnt += 1
  end
end
puts cnt