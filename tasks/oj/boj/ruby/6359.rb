t = gets.to_i
for _tc in 1..t
  n = gets.to_i
  rooms = Array.new(n + 1, false)
  for i in 1..n
    for j in 1..n
      if j % i == 0 then rooms[j] = !rooms[j] end
    end
  end
  res = 0
  for i in 1..n
    if rooms[i] then res += 1 end
  end
  puts res
end
