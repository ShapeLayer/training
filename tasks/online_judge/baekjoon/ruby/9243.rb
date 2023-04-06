n = gets.to_i
prev, done = gets.strip, gets.strip
flag = true
for i in 0..(prev.length-1)
  if n % 2 == 1 then
    if prev[i] == done[i] then
      flag = false
      break
    end
  else
    if prev[i] != done[i] then
      flag = false
      break
    end
  end
end

puts flag ? "Deletion succeeded" : "Deletion failed"